import collections
import requests
import json


class WikidataApi:

    def __init__(self, url):
        self.url = url
        self._editToken = None

    # token is here api.php?action=query&prop=info&intoken=edit&generator=allpages&format=json
    def __get_edit_token(self):
        return "+\\"  # dummy implementation!

    def wbs_getsuggestions(self, entity=None, properties=None, limit=10, cont=0, language='en', search=''):
        """
        @type entity: str or None
        @type properties: collections.Iterable[int] or None
        @type limit: int
        @type cont: int
        @type language: str
        @type search: str
        @rtype : dict
        """
        if (entity and properties) or (not entity and not properties):
            raise AttributeError("provide either a entity or properties")

        params = {'action': 'wbsgetsuggestions',
                  'format': 'json',
                  'limit': limit,
                  'continue': cont,
                  'language': language,
                  'search': search}

        if entity:
            params['entity'] = entity
        elif properties:
            params['properties'] = ','.join(map(str, properties))

        result = requests.get(self.url, params=params)

        return self._check_response_status(result)

    def get_entity_by_id(self, eid):
        params = {
            "action": "wbgetentities",
            "ids": eid,
            "format": "json"}

        result = requests.get(self.url, params=params)

        resultjson = self._check_response_status(result)
        if "-1" in resultjson["entities"]:
            return None
        else:
            entity = resultjson["entities"].values()[0]
            if "missing" in entity:
                return None
            return entity

    def create_entity(self, data, entitytype):
        params = {
            'action': 'wbeditentity',
            "data": json.dumps(data),
            "new": entitytype,
            "token": self._obtain_edit_token(),
            "format": "json"}

        result = requests.post(self.url, data=params)
        return self._check_response_status(result)

    def overwrite_entity(self, data, eid):
        params = {
            'action': 'wbeditentity',
            'id': eid,
            "data": json.dumps(data),
            "clear": True,
            "token": self._obtain_edit_token(),
            "format": "json"}

        result = requests.post(self.url, data=params)
        return self._check_response_status(result)

    def _check_response_status(self, response):
        """
        @type response: requests.Response
        @rtype : dict the Json response
        """
        if response.status_code != 200:
            raise Exception("invalid response", response, response.text)

        json_response = response.json()
        if "success" not in json_response or json_response["success"] != 1:
            errormsg = ""
            if "error" in json_response:
                errormsg += str(json_response["error"])
            raise Exception("api call failed", response, errormsg)

        return json_response

    def _obtain_edit_token(self):
        if not self._editToken:
            self._editToken = self.__get_edit_token()
        return self._editToken