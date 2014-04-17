import argparse
from propertysuggester.parser import CsvReader
from propertysuggester.utils.datatypes import Entity, Claim
from propertysuggester.utils.CompressedFileType import CompressedFileType
from propertysuggester.analyzer import TableEntitiesGenerator
from propertysuggester.utils.WikidataApi import WikidataApi

wikiApi = WikidataApi("https://www.wikidata.org/w/api.php")

def getLabelsForIdList(idList):
    result = []
    count = 0
    while(idList):
        count += 100
        if count%10000==0:
            print count + "elements processed"
        partList = idList[:100]
        idList = idList[100:]
        resultList = wikiApi.get_labels_by_ids(partList)
        for res in resultList:
            if res == "-1" or if "labels" not in res:
                continue
            result.append((res["id"], res["labels"]["en"]["value"]))
    return result


if __name__ == "__main__":
   
    parser = argparse.ArgumentParser(description="this program generates a Edit-Item-Suggestions-Table")
    parser.add_argument("input", help="The CSV input file (wikidata triple)", type=CompressedFileType('r'))
    parser.add_argument("output", help="The CSV output file (database triples: pid;qid;probablilit)")
    args = parser.parse_args()

    print "computing table..."

    generator = CsvReader.read_csv(args.input)

    table, entities = TableEntitiesGenerator.compute_table(generator)

    outputFile = open(args.output, "w")

    print "get Labels for properties..."
    IdList = []
    for pid in table:
        IdList.append("P"+str(pid))
    resultList = getLabelsForIdList(IdList)
    for entityId, label in resultList:
        outputFile.write(entityId + "," + label +"\n")

    print "get labels for items..."
    IdList = []
    for entityId in entities:
        IdList.append(entityId)
    resultList = getLabelsForIdList(IdList)
    for entityId, label in resultList:
        outputFile.write(entityId + "," + label + "\n")

    outputFile.close()
    