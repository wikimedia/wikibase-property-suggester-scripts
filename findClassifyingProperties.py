import argparse
import operator
import math
from collections import defaultdict
import AnalysisDataGenerator
from propertysuggester.parser import CsvReader
from propertysuggester.utils.datatypes import Entity, Claim
from propertysuggester.utils.CompressedFileType import CompressedFileType

numberProperties = 40 # Number of properties analyzed to find classifiers (e.g if this value is set to 40, the 40 most frequently used properties are analyzed)
numberValues = 20 # Number of analyzid values per property
minClassSize = 400 # Only classes above this size are considered relevant in analysis
minProperties = 50 # Only Properties that are used in connection with at least 50 other properties are considered in analysis

deprecatedProperties = [107, 76, 71, 77, 70, 57, 74, 168] # List of deprecated Properties that are ignored in analysis

def findClassifyingProperties(table, entities, numberProps = numberProperties, numberVals = numberValues, minClassMembers = minClassSize, minProps = minProperties):
	"""
    @type table: dict[int, dict], dict[String, list]
    @return: sorted list of tuples(property, average tfidf rating)
    """

	#Select most frequently used properties with type = wikibase-entityid:

	print "compute frequencies"

	mostFrequentlyUsed = dict(sorted(table.iteritems(), key = lambda (pid, valueDict): dict(valueDict)["appearances"], reverse = True)[:numberProps])
	for pid, valueDict in mostFrequentlyUsed.iteritems():
		del valueDict["appearances"]
		#for each property select most frequently used values
		mostFrequentlyUsed[pid] = dict(sorted(valueDict.iteritems(), key = lambda (value, items): len(items), reverse = True)[:numberVals])
	countAllPropEntries = 0
	classDict = {}
	for pid, valueDict in mostFrequentlyUsed.iteritems():
		classDict[pid] = {}
		for value, items in valueDict.iteritems():
			if len(items) > minClassMembers:
				classDict[pid][value] = defaultdict(float)
				for item in items:
					for prop in entities[item]: 
						if not prop in classDict[pid][value]:
							countAllPropEntries += 1
						classDict[pid][value][prop] += 1/float(len(items)) #compute normalized frequency for each property in each class
	
	print "computing inverse class-frequencies for " +str(countAllPropEntries) + " property entries:"

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
		if countProps > minProps:                                      # and pid not in deprecatedProperties: 
			classifierRating = classifierRating/float(countProps) #average tfidf
			overallRanking.append((pid, classifierRating))
	overallRanking = sorted(overallRanking, key = lambda (pid, averageTfIdf): averageTfIdf, reverse = True)
	return overallRanking   


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="this program finds classifying attributes in wikidata")
	parser.add_argument("input", help="The CSV input file (wikidata triple)", type=CompressedFileType("r"))
	args = parser.parse_args()
	print "computing data for analysis..."
	table, entities = AnalysisDataGenerator.computeTable(CsvReader.read_csv(args.input))
	print "finding classifying properties"
	result = findClassifyingProperties(table, entities)
	print result
	print "success"