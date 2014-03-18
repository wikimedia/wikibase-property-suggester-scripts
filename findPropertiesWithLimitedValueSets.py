import argparse
import AnalysisDataGenerator
import operator
from propertysuggester.parser import CsvReader
from propertysuggester.utils.datatypes import Entity, Claim
from propertysuggester.utils.CompressedFileType import CompressedFileType


minNumberEntities = 10 #Only Property Value Combinations that occur in over (for example) 50 items are being considered
maxNumberValues = 30 #only properies that are used in combination with under (for example) 30 different values are being considered


def findPropertiesWithLimitedValueSet(table, minEntities = minNumberEntities, maxValues = maxNumberValues):
	"""
    @type table: dict[int, dict], dict[String, list]
    @return: sorted list of tuples(property, list of tuples(value, number of times used))
    """
	propertyDict = {}
	for pid, valueDict in table.iteritems():
		if len(valueDict) < maxValues:
			for value, entityList in valueDict.iteritems():
				if value != "appearances" and len(entityList) > minEntities:
					if not pid in propertyDict:
						propertyDict[pid] = []
					propertyDict[pid].append((value, len(entityList)))
	propertyDict = sorted(propertyDict.iteritems(), key = lambda (prop, list): prop) # makes it easier to find properties / not really necessary	
	return propertyDict


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="this program finds properties with limited value-sets in wikidata")
	parser.add_argument("input", help="The CSV input file (wikidata triple)", type=CompressedFileType("r"))
	args = parser.parse_args()
	print "computing data for analysis..."
	table, entities = AnalysisDataGenerator.computeTable(CsvReader.read_csv(args.input))
	print "finding properties with limited ValueSets"
	result = findPropertiesWithLimitedValueSet(table)
	print result
	print "success"