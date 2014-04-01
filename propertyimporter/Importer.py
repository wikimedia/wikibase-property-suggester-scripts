import json
import requests
import argparse
import time

from propertysuggester.utils.WikidataApi import WikidataApi

class Importer:

    def importProperties(self, sourceApiUrl, destinationApiUrl):

        sourceApi = WikidataApi(sourceApiUrl)
        destinationApi = WikidataApi(destinationApiUrl)

        for propertyId in xrange(2, 2000):
            if propertyId % 10 == 0:
                print str(propertyId) + "/2000"
            propertyJsonSource = sourceApi.getEntityById(propertyId)
            propertyJsonDestination = destinationApi.getEntityById(propertyId)
            if propertyJsonSource is not None:
                if propertyJsonDestination is None:
                    destinationApi.createEnity(self.buildData(propertyJsonSource), "property")
                else:
                    destinationApi.overwriteEntity(self.buildData(propertyJsonSource), "P{0}".format(propertyId))
            else:
                dummy = '{"labels":{"en-gb":{"language":"en-gb","value":"dummyProperty'+str(propertyId)+'"}},"descriptions":{"en-gb":{"language":"en-gb","value":"Propertydescription"}},"datatype":"string"}'
                destinationApi.createEntity(json.loads(dummy), "property")
                #outApi.deleteById(propertyId)
        
    
    def buildData(self, propertyJson):
        props = ["aliases", "labels", "descriptions", "datatype"]

        data = {}
        
        for prop in props:
            if prop in propertyJson:
                data[prop] = propertyJson[prop]

        return data