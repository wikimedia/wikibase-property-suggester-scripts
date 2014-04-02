import json
import requests
import argparse
import time

from propertysuggester.utils.WikidataApi import WikidataApi


class Importer:
    def __init__(self, source_url, destination_url, start=1, end=1500):
        self.source_api = WikidataApi(source_url)
        self.destination_api = WikidataApi(destination_url)
        self.start = start
        self.end = end


    def import_properties(self):
        for propertyId in xrange(self.start, self.end):
            if propertyId % 10 == 0:
                print "{0}/2000".format(propertyId)
            else:
                print ".",

            source_json = self.source_api.get_entity_by_id(propertyId)
            destination_json = self.destination_api.get_entity_by_id(propertyId)
            if source_json:
                if not destination_json:
                    self.destination_api.create_entity(self.build_data(source_json), "property")
                else:
                    self.destination_api.overwrite_entity(self.build_data(source_json), propertyId)
            else:
                dummy = '{"labels":{"en-gb":{"language":"en-gb","value":"dummyProperty' + str(
                    propertyId) + '"}},"descriptions":{"en-gb":{"language":"en-gb","value":"Propertydescription"}},"datatype":"string"}'
                if not destination_json:
                    self.destination_api.create_entity(json.loads(dummy), "property")
                else:
                    self.destination_api.overwrite_entity(json.loads(dummy), propertyId)


    def check_lengthconstrains(self, prop, property_json):
        lengthconstrained = ["descriptions", "labels"]
        multilang_limits = 250  # from options.wiki

        if prop in lengthconstrained:
            for k, v in property_json[prop].items():
                if len(v['value'].encode("utf-8")) >= multilang_limits:
                    print u'Warning "{entity} - {prop} - {lang}: {value}" violates length constrains'.format(
                        entity=property_json["title"], prop=prop, lang=k, value=v['value']
                    )
                    del property_json[prop][k]


    def build_data(self, property_json):
        props = ["aliases", "labels", "descriptions", "datatype"]
        data = {}

        for prop in props:
            if prop in property_json:
                self.check_lengthconstrains(prop, property_json)
                data[prop] = property_json[prop]

        return data