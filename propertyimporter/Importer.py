import json
import requests
import argparse
import time

from propertysuggester.utils.WikidataApi import WikidataApi

class Importer:

    def importProperties(self, sourceApiUrl, destinationApiUrl):

        sourceApi = WikidataApi(sourceApiUrl)
        destinationApi = WikidataApi(destinationApiUrl)

        for propertyId in xrange(25, 2000):
            if propertyId % 10 == 0:
                print "{0}/2000".format(propertyId)
            else:
                print ".",

            propertyJsonSource = sourceApi.getEntityById(propertyId)
            propertyJsonDestination = destinationApi.getEntityById(propertyId)
            if propertyJsonSource:
                if not propertyJsonDestination:
                    destinationApi.createEntity(self.buildData(propertyJsonSource), "property")
                else:
                    destinationApi.overwriteEntity(self.buildData(propertyJsonSource), propertyId)
            else:
                dummy = '{"labels":{"en-gb":{"language":"en-gb","value":"dummyProperty'+str(propertyId)+'"}},"descriptions":{"en-gb":{"language":"en-gb","value":"Propertydescription"}},"datatype":"string"}'
                if not propertyJsonDestination:
                    destinationApi.createEntity(json.loads(dummy), "property")
                else:
                    destinationApi.overwriteEntity(json.loads(dummy), propertyId)


    def check_lengthconstrains(self, prop, propertyJson):
        lengthconstrained = ["descriptions", "labels"]
        multilang_limits = 250  # from options.wiki

        if prop in lengthconstrained:
            for k, v in propertyJson[prop].items():
                if len(v['value'].encode("utf-8")) >= multilang_limits:
                    print u'Warning "{entity} - {prop} - {lang}: {value}" violates length constrains'.format(
                        entity=propertyJson["title"], prop=prop, lang=k, value=v['value']
                    )
                    del propertyJson[prop][k]


    def buildData(self, propertyJson):
        props = ["aliases", "labels", "descriptions", "datatype"]

        data = {}

        for prop in props:
            if prop in propertyJson:
                self.check_lengthconstrains(prop, propertyJson)
                data[prop] = propertyJson[prop]

        return data