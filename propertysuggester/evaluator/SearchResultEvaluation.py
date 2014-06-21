
import random
from propertysuggester.evaluator.ResultEvaluation import ResultEvaluation

class SearchResultEvaluation(ResultEvaluation):

    def __init__(self):
        self.filename = "C:\Users\Virginia\Documents\GitHub\PropertySuggester-Python\propertysuggester\evaluator\wikidatawiki-20140526-pages-articles.csv"
        self.samplesize = 1000
        self.outputfile = "20130526_dump" + str(self.samplesize) + "6_threshold_0_.csv"

        ResultEvaluation.__init__(self, self.filename,
								  self.samplesize , self.outputfile)

	def process_entities_random(self, entity):
		propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
		random_item = random.choice(propertyIds)
		removed_list = propertyIds[:]
		removed_list.remove(random_item)
		print "\nItem {0} - {1} properties".format(entity.title, len(propertyIds))
		suggestions = self.api.wbs_getsuggestions(properties=removed_list, limit=50, cont=0)
		self.rank_suggestions(propertyIds, suggestions)

    def process_entities(self, entity):
        propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
        removed_list = propertyIds[:-1]
        print "\nItem {0} - {1} properties".format(entity.title, len(propertyIds))
        suggestions = self.api.wbs_getsuggestions(properties=removed_list, limit=50, cont=0)
        self.rank_suggestions(propertyIds, suggestions)
x = SearchResultEvaluation()
x.evaluate()

#importfile = "Wikidata-20131129161111.xml.gz.csv"