import argparse
from propertysuggester.parser import CsvReader
from propertysuggester.utils.datatypes import Entity, Claim
from propertysuggester.utils.CompressedFileType import CompressedFileType
from propertysuggester.analyzer import TableEntitiesGenerator
from collections import defaultdict

maxSuggestions = 100 # threshold that suggestions in the results have to pass

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
        propList = list(entities[entity])
        #for pid1 in table:
        for pid1 in [569]:
            if pid1 not in propList:
                probabilitySum = 0
                for pid2 in propList:
                    probabilitySum += table[pid2][pid1]/float(table[pid2]["appearances"])
                averageProbability = probabilitySum/len(propList)
                if len(editItemSuggestionsTable[pid1]) < maxSuggestions:
                    editItemSuggestionsTable[pid1].append((averageProbability, entity))
                else:
                    if min(editItemSuggestionsTable[pid1])[0] < averageProbability:
                        editItemSuggestionsTable[pid1][editItemSuggestionsTable.index(min(editItemSuggestionsTable[pid1]))] = (entity, averageProbability)
    #print editItemSuggestionsTable
    for prop, entityList in editItemSuggestionsTable.iteritems():
        print "\n"+ str(prop)
        print entityList

