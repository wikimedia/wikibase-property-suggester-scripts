import requests

class WikidataApi:
    def __init__(self, url):
        self.url = url

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
            params['properties'] = '|'.join(map(str, properties))

        result = requests.get(self.url + "/api.php", params=params)
        return result.json()

    def wb_getentities(self, entityid="",language = "en"):
        # action=wbgetentities&format=json&ids=P35

        params = {'action': 'wbgetentities', 'format': 'json',
                  'language': language, 'ids': entityid}

        result = requests.get(self.url + "/api.php", params=params)
        return result.json()

    def wb_searchentities(self,letter = "",type = 'property',language ='en', continues=0 ):
        params ={'action': 'wbsearchentities', 'format': 'json', 'language': language, 'type': type, 'search' : letter, 'continue': continues, 'limit': 50}
        result = requests.get(self.url + "/api.php", params=params)
        return result.json()