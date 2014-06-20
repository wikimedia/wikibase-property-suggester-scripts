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
        ResultEvaluation.__init__(self, "Y:\Documents\GitHub\PropertySuggester-Python\wikidatawiki-20140526-pages-articles.csv", 1000, "20130526_dump_1000_first_letter.csv")
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


    def get_all_letters(self):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        result_dict ={}
        for letter in letters:
            result_dict[letter] = 0

            total = self.api.wb_searchentities(letter=letter)
            print total
            while "search-continue" in total:
                print total["search-continue"]
                continues = total["search-continue"]
                result = total["search"]

                length = len(result)
                result_dict[letter] += length
                total = self.api.wb_searchentities(letter=letter, continues=continues)

        print str(result_dict)
        summe = 0
        for letter, amount in result_dict.items():
            summe += amount
        print "insgesamte anzahl properties: " + str(summe)


x = FirstLetterResultEvaluation()
x.get_all_letters()

#importfile = "Wikidata-20131129161111.xml.gz.csv"