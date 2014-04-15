import argparse
from propertysuggester.parser import CsvReader
from propertysuggester.utils.datatypes import Entity, Claim
from propertysuggester.utils.CompressedFileType import CompressedFileType
from propertysuggester.utils.WikidataApi import WikidataApi
from propertysuggester.analyzer import TableEntitiesGenerator
from collections import defaultdict

threshold = 0.3 # threshold that suggestions in the results have to pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program generates a Edit-Item-Suggestions-Table")
    parser.add_argument("input", help="The CSV input file (wikidata triple)", type=CompressedFileType('r'))
    args = parser.parse_args()

    print "computing table..."

    generator = CsvReader.read_csv(args.input)

    table, entities = TableEntitiesGenerator.compute_table(generator)

    editItemSuggestionsTable = defaultdict(list)

    itemCount=0

    for entity in entities:
        itemCount +=1
        if itemCount%100000 == 0:
            print str(itemCount)
        propList = entities[entity]
        for pid1 in table:
            if pid1 not in propList:
                probabilitySum = 0
                for pid2 in propList:
                    probabilitySum += table[pid2][pid1]/table[pid2]["appearances"]
                averageProbability = probabilitySum/len(propList)
                if (averageProbability >= threshold):
                    editItemSuggestionsTable[pid1].append(entity.title)
    for prop, entityList in editItemSuggestionsTable.iteritems():
        print "\n"+ str(p)
        print entityList

