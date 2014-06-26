
import random
from propertysuggester.evaluator.ResultEvaluation import ResultEvaluation

classifyingAttributes = [31, 5]

class SearchResultEvaluation(ResultEvaluation):

    def __init__(self):
        self.filename = "E:\Moritz\Desktop\Bachelorprojekt\wikidatawiki-20140526-pages-articles.xml\dump.csv"
        self.samplesize = 1000
        self.outputfile = "ClassifyingPropertiesEvaluation20130526_dump" + str(self.samplesize) + "2To6_threshold_0_.csv"

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
        propertyValuePairs = [] 
        propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
        for claim in entity.claims:
            if claim.property_id in classifyingAttributes:
                propertyValuePairs.append("("+ str(claim.property_id) + ";" + str(claim.value)[1:] + ")")
            else:
                propertyValuePairs.append("("+ str(claim.property_id) + ";" + "0" + ")")
        removed_list = propertyValuePairs[:-1]
        print removed_list
        print "\nItem {0} - {1} properties".format(entity.title, len(propertyIds))
        suggestions = self.api.wbs_getsuggestions(properties=removed_list, limit=50, cont=0)
        self.rank_suggestions(propertyIds, suggestions)
x = SearchResultEvaluation()
x.evaluate()

#importfile = "Wikidata-20131129161111.xml.gz.csv"