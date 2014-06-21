__author__ = 'Virginia'
from propertysuggester.evaluator.ResultEvaluation import ResultEvaluation
from propertysuggester.utils.WikidataApi import WikidataApi
from Entity import Entity
import csv
from manuelle_auswertung import UserFeedbackEvaluation
import json


class Missing_Evaluation(ResultEvaluation):
    def __init__(self):
        self.api = WikidataApi("http://suggester.wmflabs.org/w/")
        self.ranking_amounts = None
        self.filename = "C:\Users\Virginia\Documents\GitHub\PropertySuggester-Python\propertysuggester\evaluator\wikidatawiki-20140526-pages-articles.csv"
        self.samplesize = 1000
        self.outputfile = "20130526_dump" + str(self.samplesize) + ".csv"
        self.ranked_dict = {}
        self.foundMissing = 0
        self.notFoundMissing = 0
        ResultEvaluation.__init__(self, self.filename, self.samplesize , self.outputfile)

    # input: entity, missing_properties
    # fuer jede property schauen, wo sie in Liste auftaucht

    def get_missing(self, eval_list):
        entity_dict= {}
        for entity in eval_list:
            if entity.missing == "[]":
                continue
            entity_dict[entity.entity] = str(entity.missing)
        #print str(entitity_dict)
        print str(len(entity_dict))
        return entity_dict

    def find_missing(self, entity_dict):
        for entity, missing in entity_dict.items():
            entity_json = self.api.wb_getentities(entityid=entity, language="en")
            entity_description = entity_json["entities"][str(entity)]
            claims = entity_description["claims"]
            self.process_entities(entity_description, json.loads(missing))
        print "AVG of found ones " + str(float(self.foundMissingPropertiesRankSum)/self.foundMissingProperties)
        print "Total amount of found(dealed with) missing properties " + str(self.foundEntities)
        print "Total amount entities: " +str(len(entity_dict))
        print " Found with property_suggester: "+  str(self.foundMissingProperties) + " " + str(self.foundMissing) +"  not found: " + str(self.notFoundMissing)

    def process_entities(self, entity, missing_dict):

            missing_properties = [int(str(item.keys()[0])[1:]) for item in missing_dict]
            print "\nMissing properties {0} for entity {1}".format(missing_properties,entity["title"])
           # propertyIds = [int(prop_id[1:]) for prop_id in entity["claims"].keys()]  # get ids from claims
            #print "Property Ids: {0}".format(propertyIds)
            print "Item {0} -  properties".format(entity["title"])
            entity_string = entity["title"][5:]
            suggestions = self.api.wbs_getsuggestions(entity=entity_string, limit=50, cont=0)
            self.rank_suggestions(entity["title"],suggestions, missing_properties)

    def rank_suggestions(self, entity, suggestions, missing_properties):
        rank = 0
        self.appearsWithinFirst50 = False
        entity = entity[5:]  # cut off "Item:"
        local_found_missing = 0
        for suggestion in suggestions["search"]:
            rank += 1
            print "currently checking: " + suggestion["id"][1:]
            #print str(missing_properties)
            if int(suggestion["id"][1:]) in missing_properties:
                print "Found missing property " + str(suggestion["id"][1:]) + " at rank " + str(rank)
                local_found_missing += 1
                if entity not in self.ranked_dict:
                    self.ranked_dict[entity] = [{"missing": suggestion["id"], "rank": rank}]
                else:
                    self.ranked_dict[entity].append({"missing": suggestion["id"], "rank": rank})

                self.foundMissingPropertiesRankSum += rank
                self.foundMissingProperties += 1


        not_found_local = len(missing_properties)- local_found_missing
        self.foundMissing += local_found_missing
        self.notFoundMissing += not_found_local

    def print_result(self):
        print str(self.ranked_dict)
        with open("missing_analysis___2.csv","wb") as csv_file:
            missing_writer = csv.writer(csv_file, delimiter=';',
                                       quotechar='|')
            missing_writer.writerow(["item","missing","rank"])
            for item, result in self.ranked_dict.items():
                for entry in result:
                   # [{'rank': 12, 'missing': u'P1082'},x,y]
                    missing = entry["missing"]
                    rank =entry["rank"]
                    missing_writer.writerow([item, missing, rank])





    def make_readableoutput(self, entity_missing_dict):
        result_dict = {}
        with open("missing_readable.csv","wb") as csv_file:
            missing_writer = csv.writer(csv_file, delimiter=';',
                                       quotechar='|')
            for entity, missing in entity_missing_dict.items():
                entity_json = self.api.wb_getentities(entityid=entity, language="en")
                label =  entity_json["entities"][entity]["labels"]["en"]["value"]
                missing = json.loads(missing)
                for i in missing:
                    for property, description in i.items():
                        missing_writer.writerow([entity, label.encode("utf-8"), property, description.encode("utf-8")])








luser = UserFeedbackEvaluation()
eval_list = luser.preprocess_file()
m = Missing_Evaluation()
entity_dict = m.get_missing(eval_list)
#m.make_readableoutput(entity_dict)
m.find_missing(entity_dict)
m.print_result()