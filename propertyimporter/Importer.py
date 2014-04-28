import json
import requests
import argparse
import time

from propertysuggester.utils.WikidataApi import WikidataApi
from propertysuggester.utils.WikidataApi import ServiceUnavailableError

class Importer:
    def importProperties(self, inApiUrl, outApiUrl):
        inApi = WikidataApi(inApiUrl)
        outApi = WikidataApi(outApiUrl)

        for propertyId in xrange(2, 2000):

            retry = True;
            while retry:
                try:
                    propertyJson = inApi.getEntityById(propertyId)
                    retry = False
                except ServiceUnavailableError as e:
                    retry = True
                    time.sleep(3)


            print propertyJson
            if propertyJson != None and False :
                outApi.newPropertyByData(self.buildData(propertyJson))
            else :
                dummy = '{"labels":{"en-gb":{"language":"en-gb","value":"dummyProperty'+str(propertyId)+'"}},"descriptions":{"en-gb":{"language":"en-gb","value":"Propertydescription"}},"datatype":"string"}'
                outApi.newPropertyByData(json.loads(dummy))
                #outApi.deleteById(propertyId)
        
    
    def buildData(self, propertyJson):
        props = ["aliases", "labels", "descriptions", "datatype"]

        data = {}
        
        for prop in props:
            if prop in propertyJson:
                data[prop] = propertyJson[prop]

        return data