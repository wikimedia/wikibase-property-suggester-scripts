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


def generate_random_integers(ids):
	counter = 0
	while counter < 2*sampleSize:
		#ids.append(random.randint(0, 100))
		ids.append(random.randint(0, 6656575))
		counter += 1




def handle_found_suggestion():
	global itemsOnFirst50PositionSum, itemsOnFirst50Count, appearsWithinFirst50, ranking_amounts
	print "Found suggestion at rank " + str(rank)
	ranking_amounts[rank] += 1
	itemsOnFirst50PositionSum += rank
	itemsOnFirst50Count += 1
	appearsWithinFirst50 = True

def write_output_file(ranking_amounts):

	with open("_output.tsv", 'wb') as csvfile:
		rankingwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		rankingwriter.writerow(["rank","amount"])
		for key, value in ranking_amounts.iteritems():
			rankingwriter.writerow([str(key), str(value)])
		rankingwriter.writerow([">50" , str(itemsBeyond50Count)])



sampleSize = 10

random.seed(1)  # always choose the same random objects
ids = []
generate_random_integers(ids)
print ids
# adding 10 random integers to list

itemsOnFirst50PositionSum = 0
itemsOnFirst50Count = 0
itemsBeyond50Count = 0
global ranking_amounts
ranking_amounts = defaultdict(lambda: 0)
current_item_number = 0
totalItems = 0
global foundEntities
foundEntities = 0

with open("wikidatawiki-20131021-pages-articles.csv", "r") as f:
#with open("Wikidata-20131129161111.xml.gz.csv", "r") as f:
	for entity in CsvReader.read_csv(f):

		if not foundEntities >= sampleSize:
			if current_item_number in ids and len(entity.claims) > 1:

				propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
				print "\nItem " + entity.title + ":"
				#api = WikidataApi("http://127.0.0.1/devrepo")
				api = WikidataApi("http://suggester.wmflabs.org/wiki")
				suggestions = api.wbs_getsuggestions(properties=propertyIds, limit=10, cont=31)

				rank = 0
				appearsWithinFirst50 = False
				for suggestion in suggestions["search"]:
					rank += 1
					if int(propertyIds[-1]) == int(suggestion["id"][1:]):
						handle_found_suggestion()

						foundEntities += 1
						break
				if not appearsWithinFirst50:
					itemsBeyond50Count += 1
					foundEntities+= 1
					print "Rank could not be determined within first 50"
		current_item_number += 1


	write_output_file(ranking_amounts)
f.close()
print "Size of Entities in Output: " + str(foundEntities)
print " SampleSize the user requested: " + str(sampleSize)
print "Total amount of items in dump: "+ str(current_item_number)
print "We extract the last added property and check at which position it would have been suggested (based on remaining properties)."
print "Average rank of extracted properties positioned within the first 50 suggestions: " + str(float(itemsOnFirst50PositionSum) / itemsOnFirst50Count)
print "Count of extracted properties not positioned within the first 50 suggestions: " + str(itemsBeyond50Count)


f.close()
