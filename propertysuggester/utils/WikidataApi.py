import requests
import json


class WikidataApi:
    # token is here http://localhost/devrepo/core/api.php?action=query&prop=info&intoken=edit&generator=allpages&format=json

    def __init__(self, url):
        self.url = url + "/api.php"
        self._editToken = None

    def _get_edit_token(self):
        return "+\\"  # dummy implementation!

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
        self._check_response_status(result)
        return result.json()


    def _check_response_status(self, response):
        if response.status_code != 200:
            raise Exception("invalid response", response, response.text)
        json_response = response.json()
        if not "success" in json_response:
            errormsg = ""
            if "error" in json_response:
                errormsg += str(json_response["error"])
            raise Exception("api call failed", response, errormsg)


    def obtainEditToken(self):
        if not self._editToken:
            self._editToken = self._get_edit_token()
        return self._editToken


    def create_entity(self, data="", new=""):
        params = {
            'action': 'wbeditentity',
            "data": json.dumps(data),
            "new": new,
            "token": self.obtainEditToken(),
            "format": "json"}

        result = requests.post(self.url, data=params)
        self._check_response_status(result)
        return result.json()


    def overwrite_entity(self, data, eid):

        params = {
            'action': 'wbeditentity',
            'id': "P{0}".format(eid),
            "data": json.dumps(data),
            "clear": True,
            "token": self.obtainEditToken(),
            "format": "json"}

        result = requests.post(self.url, data=params)
        self._check_response_status(result)
        return result.json()


    def get_entity_by_id(self, pid):

        params = {
            "action": "wbgetentities",
            "ids": "P{0}".format(pid),
            "format": "json"}

        result = requests.get(self.url, params=params)
        self._check_response_status(result)

        resultJson = result.json()

        if "-1" in resultJson["entities"]:
            return None
        else:
            return resultJson["entities"].values()[0]


