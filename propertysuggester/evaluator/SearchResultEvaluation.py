"""
read_csv returns a generator that yields the tuple (title, [(p1, dt1, v1), (p2, dt1, v2),..])
where
p_n is a property
d_n is a datatype
v_n is a value

usage:
with open("file.csv", "r") as f:
     for title, claim in read_csv(f):
          do_things()

"""
from collections import defaultdict

import random
import json
import urllib2
import csv
from propertysuggester.parser import CsvReader
from propertysuggester.utils.WikidataApi import WikidataApi

class Evaluator():
    def __init__(self):
        self.inputfile = ""
        self.outputfile = "_output.csv"
        self.samplesize = 10
        self.itemsBeyond50Count = 0
        self.itemsOnFirst50PositionSum = 0
        self.itemsOnFirst50Count = 0
        self.appearsWithinFirst50 = False
        self.ranking_amounts = defaultdict(lambda: 0)
        self.ids = []
        self.foundEntities = 0
        
    def generate_random_integers(self):
        random.seed(1)
        counter = 0
        while counter < 2 * self.samplesize:
            self.ids.append(random.randint(0, 87))
            #ids.append(random.randint(0, 6656575))
            counter += 1


    def handle_found_suggestion(self, rank):
        
        print "Found suggestion at rank " + str(rank)
        self.ranking_amounts[rank] += 1
        self.itemsOnFirst50PositionSum += rank
        self.itemsOnFirst50Count += 1
        self.appearsWithinFirst50 = True


    def write_output_file(self, ranking_amounts):
        with open("_output.tsv", 'wb') as csvfile:
            rankingwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rankingwriter.writerow(["rank", "amount"])
            for key, value in self.ranking_amounts.iteritems():
                rankingwriter.writerow([str(key), str(value)])
            rankingwriter.writerow([">50", str(self.itemsBeyond50Count)])


    def determine_ranks(self, current_item_number, foundEntities):
        with open("Wikidata-20131129161111.csv", "r") as f:
        #with open("Wikidata-20131129161111.xml.gz.csv", "r") as f:
            for entity in CsvReader.read_csv(f):
                if not foundEntities >= self.samplesize:
                    if current_item_number in self.ids and len(entity.claims) > 1:
                        propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
                        removed_list = propertyIds[:-1]
                        print "\nItem " + entity.title + ":"
                        api = WikidataApi("http://127.0.0.1/devrepo")
                        #api = WikidataApi("http://suggester.wmflabs.org/wiki")
                        suggestions = api.wbs_getsuggestions(properties=removed_list, limit=50, cont=0)
                        rank = 0
                        self.appearsWithinFirst50 = False

                        for suggestion in suggestions["search"]:
                            rank += 1
                            if int(propertyIds[-1]) == int(suggestion["id"][1:]):
                                self.handle_found_suggestion(rank)
                                foundEntities += 1
                                break
                        if not self.appearsWithinFirst50:
                            self.itemsBeyond50Count += 1
                            foundEntities += 1
                            print "Rank could not be determined within first 50"
                current_item_number += 1
        f.close()
        return current_item_number, f, foundEntities

    def evaluate(self):
        self.generate_random_integers()
        print self.ids
        current_item_number = 0
        foundEntities = 0

        current_item_number, f, foundEntities = self.determine_ranks(current_item_number, foundEntities)



        self.write_output_file(self.ranking_amounts)

        print "Size of Entities in Output: " + str(foundEntities)
        print " samplesize the user requested: " + str(self.samplesize)
        print "Total amount of items in dump: " + str(current_item_number)
        print "We extract the last added property and check at which position it would have been suggested (based on remaining properties)."
        if self.itemsOnFirst50Count > 0 and self.itemsOnFirst50PositionSum > 0:
            print "Average rank of extracted properties positioned within the first 50 suggestions: " + str(
                float(self.itemsOnFirst50PositionSum) / self.itemsOnFirst50Count)
        print "Count of extracted properties not positioned within the first 50 suggestions: " + str(self.itemsBeyond50Count)

        f.close()



x = Evaluator()
x.evaluate()