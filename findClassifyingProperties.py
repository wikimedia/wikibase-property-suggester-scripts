import argparse
from collections import defaultdict
import cPickle as pickle
import operator
import math
from collections import Counter
from collections import defaultdict
from propertysuggester.parser import CsvReader
from propertysuggester.utils.datatypes import Entity, Claim
from propertysuggester.utils.CompressedFileType import CompressedFileType


minNumberEntities = 50
MaxNumberValues = 30

deprecatedProperties = [107, 76, 71, 77, 70, 57, 74, 168]

def computeTable(generator):
	i = 0
	table = {}
	entities = {}
	for entity in generator:
		entities[entity.title] = []
		i+=1
		if i%750000 == 0:
			print str(i/75000.0)+"%"
		for claim in entity.claims:
			pid = claim.property_id
			if claim.datatype == "wikibase-entityid" and pid not in deprecatedProperties:   #classes are represented by wikibase-entities
				if not pid in table:
					table[pid] = defaultdict(int)
				if not pid in entities[entity.title]:  
					table[pid]["appearances"] += 1   #count occurences for each property
					entities[entity.title].append(pid)
				if not claim.value in table[pid]:  #for each property keep track of occuring values and entities described by specific property,value combinations
					table[pid][claim.value] = []
				table[pid][claim.value].append(entity.title) #specific (entity, property, value) - triple can only occur once - so no need to check for existance here
	return table, entities

def findClassifyingProperties(table, entities, numberProperties, numberValues):
	#Select top 10 most frequently used properties with type = wikibase-entityid:
	print "compute frequency"
	mostFrequentlyUsed = dict(sorted(table.iteritems(), key = lambda (pid, valueDict): dict(valueDict)["appearances"], reverse = True)[:numberProperties])
	for pid, valueDict in mostFrequentlyUsed.iteritems():
		del valueDict["appearances"]
		mostFrequentlyUsed[pid] = dict(sorted(valueDict.iteritems(), key = lambda (value, items): len(items), reverse = True)[:numberValues])
	countAllPropEntries = 0
	classDict = {}
	for pid, valueDict in mostFrequentlyUsed.iteritems():
		classDict[pid] = {}
		for value, items in valueDict.iteritems():
			if len(items)>250:
				classDict[pid][value] = defaultdict(float)
				for item in items:
					for prop in entities[item]: 
						if not prop in classDict[pid][value]:
							countAllPropEntries += 1
						classDict[pid][value][prop] += 1/float(len(items)) #compute normalized frequency for each property in each class
	print "Number of Property Entries:" + str(countAllPropEntries)  

	print "compute inverse class-frequency"

	overallRanking = []
	progress = 0
	for pid, valueDict in classDict.iteritems():
		countProps = 0
		classifierRating = 0
		for value, propertyDict in valueDict.iteritems():
			for prop, tf in propertyDict.iteritems(): #compute tfid for each property in each class
				countProps += 1
				progress += 1
				if countProps%500 == 0:
					print str(progress) + " / " + str(countAllPropEntries) 
				classesWithProp = 0
				for value, propertyDict in valueDict.iteritems(): 
					if prop in propertyDict:
						classesWithProp +=1
				classifierRating += tf * math.log(len(valueDict)/classesWithProp) 
		if countProps > 50:                                      # and pid not in deprecatedProperties: 
			classifierRating = classifierRating/float(countProps) #average tfidf
			overallRanking.append((pid, classifierRating))
	overallRanking = sorted(overallRanking, key = lambda (pid, averageTfIdf): averageTfIdf, reverse = True)
	return overallRanking   

def findPropertiesWithLimitedValueSet(table, maxNumberValues, minNumberEntities):
	propertyDict = {}
	for pid, valueDict in table.iteritems():
		if len(valueDict) <= maxNumberValues:
			for value, entityList in valueDict.iteritems():
				if value != "appearances" and len(entityList) > minNumberEntities:
					if not pid in propertyDict:
						propertyDict[pid] = []
					propertyDict[pid].append((value, len(entityList)))
	print propertyDict


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="this program finds classifying attributes in wikidata")
	parser.add_argument("input", help="The CSV input file (wikidata triple)", type=CompressedFileType("r"))
	args = parser.parse_args()
	print "computing table..."
	table, entities = computeTable(CsvReader.read_csv(args.input))
	print "finding properties with limited ValueSets"
	findPropertiesWithLimitedValueSet(table, MaxNumberValues, minNumberEntities)
	print "finding classifying properties"
	result = findClassifyingProperties(table, entities, 40, 20)
	print result
	print "success"