import random
import csv
from propertysuggester.parser import CsvReader
from propertysuggester.utils.WikidataApi import WikidataApi

class ResultEvaluation:
    def __init__(self, inputfile, samplesize, outputfile):
        self.inputfile = inputfile
        self.samplesize = samplesize
        self.outputfile = outputfile
        self.itemsBeyond50Count = 0
        self.foundMissingPropertiesRankSum = 0
        self.foundMissingProperties = 0
        self.appearsWithinFirst50 = False
        self.ranking_amounts = {i: 0 for i in range(1,51)}
        self.random_ids = []
        self.foundEntities = 0
        self.api = WikidataApi("http://127.0.0.1/devrepo/wiki")

    def generate_random_integers(self):
        random.seed(2)
        counter = 0
        while counter < 100 * self.samplesize:
            self.random_ids.append(random.randint(0, 10957764))
            counter += 1

    def write_output_file(self, ranking_amounts):
        with open(self.outputfile, 'wb') as csvfile:
            rankingwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            rankingwriter.writerow(["rank", "amount"])
            for key, value in self.ranking_amounts.iteritems():
                rankingwriter.writerow([str(key), str(value)])
            rankingwriter.writerow([">50", str(self.itemsBeyond50Count)])
        csvfile.close()

    def rank_suggestions(self, propertyIds, suggestions):
        rank = 0
        self.appearsWithinFirst50 = False
        for suggestion in suggestions["search"]:
            rank += 1
            if int(propertyIds[-1]) == int(suggestion["id"][1:]):
                self.handle_found_suggestion(rank)
                break
        if not self.appearsWithinFirst50:
            self.itemsBeyond50Count += 1
            self.foundEntities += 1
            print "Rank could not be determined within first 50"

    def handle_found_suggestion(self, rank):
        print "Found suggestion at rank " + str(rank)
        self.ranking_amounts[rank] += 1
        self.foundMissingPropertiesRankSum += rank
        self.foundMissingProperties += 1
        self.foundEntities += 1
        self.appearsWithinFirst50 = True

    def process_entities(self, entity):
        raise NotImplementedError("This method is abstract, please implement.")


    def determine_ranks(self):
        with open(self.inputfile, "r") as f:
            current_item_count = 0
            processed_items = 0
            for entity in CsvReader.read_csv(f):
                if self.foundEntities < self.samplesize:
                    if current_item_count in self.random_ids and len(entity.claims) <= 6 and len(entity.claims) > 1:
                        print "Processed Items: {0}".format(processed_items)
                        self.process_entities(entity)
                        processed_items += 1
                current_item_count += 1
        f.close()
        return current_item_count

    def print_output(self, current_item_number):
        print "Size of Entities in Output: " + str(self.foundEntities)
        print " samplesize the user requested: " + str(self.samplesize)
        print "Total amount of items in dump: " + str(current_item_number)
        print "We extract the last added property and check at which position it would have been suggested (based on remaining properties)."
        if self.foundMissingProperties > 0 and self.foundMissingPropertiesRankSum > 0:
            print "Average rank of extracted properties positioned within the first 50 suggestions: " + str(
                float(self.foundMissingPropertiesRankSum) / self.foundMissingProperties)
        print "Count of extracted properties not positioned within the first 50 suggestions: " + str(
            self.itemsBeyond50Count)

    def evaluate(self):
        self.generate_random_integers()
        #print "Ids: {0}".format(sorted(self.random_ids))
        current_item_number = self.determine_ranks()
        self.write_output_file(self.ranking_amounts)
        self.print_output(current_item_number)
