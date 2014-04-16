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

    """
    resultList = getLabelsForIdList(["P31", "P19", "Q2"])
    print resultList
    """
    Idlist = []
    for pid in table:
        Idlist.append("P"+str(pid))
    resultList = getLabelsForIdList(IdList)
    print resultList
    """
    print "finding property Labels"
    propertyCount = 0
    for pid in table:
        propertyCount+=1
        if propertyCount%100 == 0:
            print propertyCount + " Properties processed"
        outputFile.write(str(prop) +  "," + wikiApi.get_entity_by_id("P{0}".format(pid))["labels"]["en"]["value"] + "\n")
    outputFile.write("\n Item-Labels: \n")
    itemCount = 0
    for qid in entities:
        itemCount+=1
        if itemCount%100 == 0:
            print itemCount + " Items processed"
        outputFile.write(qid[1:] +  "," + wikiApi.get_entity_by_id(qid)["labels"]["en"]["value"] + "\n")
    outputFile.close()
"""