
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

import random
from propertysuggester.evaluator.ResultEvaluation import ResultEvaluation

class SearchResultEvaluation(ResultEvaluation):
	def __init__(self):
		ResultEvaluation.__init__(self, "Y:\Documents\GitHub\PropertySuggester-Python\wikidatawiki-20140526-pages-articles.csv",
								  1000 ,"20130526_dump_1000_random_new_algorithm_5_threshold.csv")

	def process_entities(self, entity):
		propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
		random_item = random.choice(propertyIds)
		removed_list = propertyIds[:]
		removed_list.remove(random_item)
		print "\nItem {0} - {1} properties".format(entity.title, len(propertyIds))
		suggestions = self.api.wbs_getsuggestions(properties=removed_list, limit=50, cont=0)
		self.rank_suggestions(propertyIds, suggestions)

x = SearchResultEvaluation()
x.evaluate()

#importfile = "Wikidata-20131129161111.xml.gz.csv"