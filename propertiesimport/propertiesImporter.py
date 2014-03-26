import requests
import argparse
import time
import xml.dom.minidom
from xml.dom.minidom import Node

class Importer:
    def importProperties(self, file):
        dom = xml.dom.minidom.parse(file)
        pages = dom.getElementsByTagName("page")

        i = 2
        for page in pages:
            pageId = int(page.getElementsByTagName('title')[0].childNodes[0].nodeValue[10:])
            while(i < pageId):
                self.doImport('{"labels":{"en-gb":{"language":"en-gb","value":"dummyProperty'+str(i)+'"}},"descriptions":{"en-gb":{"language":"en-gb","value":"Propertydescription"}},"datatype":"string"}')
                i += 1
            self.doImport(page.getElementsByTagName('text')[0].childNodes[0].nodeValue)
            i += 1

    def doImport(self, text):
        propertyparams = {
            'action' : 'wbeditentity',
            'data' : text.replace('"label"', '"labels"').replace('"description"','"descriptions"').replace('"entity"','"entities"'), #studpid stupids
            'new' : 'property',
            'token' : "+\\",# token is here http://localhost/devrepo/core/api.php?action=query&prop=info&intoken=edit&generator=allpages&format=json
            'format' : 'jsonfm'}

        result = requests.post("http://localhost/devrepo/core/api.php", data=propertyparams)
        print text.decode("utf-8")
        print result.text.encode("utf-8")[:2000]
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program reads from a file of property XML exports and imports the properties using wbeditentity api call.")
    parser.add_argument("input", help="The XML input file")
    args = parser.parse_args()
    
    start = time.time()
    
    a = Importer()
    a.importProperties(args.input)
    
    print "total time: %.2fs"%(time.time() - start)
    imp = Importer()
    