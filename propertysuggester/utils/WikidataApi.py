import requests
import json

class WikidataApi:

    # token is here http://localhost/devrepo/core/api.php?action=query&prop=info&intoken=edit&generator=allpages&format=json

    def __init__(self, url):
        self.url = url + "/api.php"
        self.editToken = ""

    def getEditToken():
        pass

    def wbs_getsuggestions(self, entity="", properties=(), limit=10, cont=0, language='en', search=''):
        """
        @rtype : dict
        @type entity: str
        @type properties: tuple[int] or list[int]
        @type limit: int
        @type cont: int
        @type language: str
        @type search: str
        """
        if (entity and properties) or (not entity and not properties):
            raise AttributeError("provide either a entity or properties")

        params = {'action': 'wbsgetsuggestions', 'format': 'json',
                  'limit': limit, 'continue': cont,
                  'language': language, 'search': search}

        if entity:
            params['entity'] = entity
        elif properties:
            params['properties'] = ','.join(map(str, properties))

        result = requests.get(self.url, params=params)
        self._checkResponseStatus(result)
        return result.json()

    def _checkResponseStatus(self, response):
        if response.status_code != 200:
            raise Exception("invalid response", response)

    def obtainEditToken(self):
        self.editToken = "+\\"

    def createEntity(self, data="", new=""):

        if self.editToken == "":
            self.obtainEditToken()

        params = {
            'action' : 'wbeditentity',
            "data" : json.dumps(data),
            "new" : new,
            "token" : self.editToken,
            "format" : "json" }

        result = requests.post(self.url, data=params)
        self._checkResponseStatus(result)
        print result.json()
        return result.json()

    def overwriteEntity(self, data, eid):

        if self.editToken == "":
            self.obtainEditToken()

        params = {
            'action' : 'wbeditentity',
            'id' : eid,
            "data" : json.dumps(data),
            "clear" : True,
            "token" : self.editToken,
            "format" : "json" }

        result = requests.post(self.url, data=params)
        self._checkResponseStatus(result)
        return result.json()

    def getEntityById(self, pid):

        params = {
            "action" : "wbgetentities",
            "ids" : "P{0}".format(pid),
            "format" : "json"}

        result = requests.post(self.url, data=params)
        self._checkResponseStatus(result)

        resultJson = result.json()

        if "-1" in resultJson["entities"]:
            return None
        else:
            return resultJson["entities"].values()[0]


