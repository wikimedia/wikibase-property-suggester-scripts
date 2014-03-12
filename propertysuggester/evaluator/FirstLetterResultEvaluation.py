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

from propertysuggester.evaluator.ResultEvaluation import ResultEvaluation
from propertysuggester.parser import CsvReader

class FirstLetterResultEvaluation(ResultEvaluation):

    def __init__(self):
        ResultEvaluation.__init__(self, "C:\Users\Virginia\Documents\GitHub\wikidatawiki-20131021-pages-articles.csv", 10, "Resultoutput_letter.csv")
        self.property_dic = {}


    def get_first_letter(self, property_id):
        if property_id in self.property_dic:
            first_letter = self.property_dic[property_id]
        else:
            property_json = self.api.wb_getentities(entityid=property_id, language="en")
            property_description = property_json["entities"][str(property_id)]["labels"]["en"]["value"]
            first_letter = property_description[0]
            self.property_dic[property_id] = first_letter
        return first_letter

    def process_entities(self, entity):
        propertyIds = [claim.property_id for claim in entity.claims]  # get ids from claims
        removed_list = propertyIds[:-1]
        removed_property_id = propertyIds[-1]
        property_id = "P" + str(removed_property_id)
        print "\nItem " + entity.title + ":"
        first_letter = self.get_first_letter(property_id)  #api = WikidataApi("http://suggester.wmflabs.org/wiki")
        suggestions = self.api.wbs_getsuggestions(properties=removed_list, limit=50, cont=0, search=first_letter)
        self.rank_suggestions( propertyIds, suggestions)




x = FirstLetterResultEvaluation()
x.evaluate()

#importfile = "Wikidata-20131129161111.xml.gz.csv"