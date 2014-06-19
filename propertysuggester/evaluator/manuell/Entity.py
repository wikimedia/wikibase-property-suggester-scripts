__author__ = 'Virginia'
import json


class Entity:
    def __init__(self, row, entity_id):
        self.id = entity_id
        self.timestamp = row[1]
        self.user = row[2]
        self.entity = row[3]
        property_json = json.loads(row[4])
        self.properties = [Property(p) for p in property_json]

        suggestion_json = json.loads(row[5])
        self.suggestions = [Suggestion(s, i) for i, s in enumerate(suggestion_json)]
        missing_json = json.loads(row[6])
        self.missing = [Missing(m) for m in missing_json]
        self.missing = row[6]
        self.overall = row[7]
        self.opinion = row[8]

    def __str__(self):

        return "\n".join(("entity: "+ str(self.entity),
                          "timestamp " + str(self.timestamp),
                          "user: " + str(self.user),
                          "properties: " + str(map(str, self.properties)),
                          "suggestions" + str(map(str, self.suggestions)),
                          "missing: " + str(map(str, self.missing)),
                            "opinion" + str(self.opinion),
                           "overall" + str(self.overall)))


class Suggestion:
    def __init__(self, suggestion, suggestion_id):
        self.position = suggestion_id
        self.suggestion_id = suggestion["id"]
        self.suggestion_label = suggestion["label"]
        self.rating = suggestion["rating"]
        self.probability = suggestion["probability"]

    def __str__(self):
        return str(self.__dict__)


class Property:
    def __init__(self, property_data):
        self.property_id = property_data["id"]
        if "label" in property_data:
            self.property_label = property_data["label"]
        else:
            self.property_label = str(self.property_id)

    def __str__(self):
        return str(self.__dict__)


class Missing:
    def __init__(self, missing_object):
        missing_item = missing_object.items()
        if missing_item:
            self.missing_property = missing_item[0][0]
            self.missing_label = missing_item[0][1]

    def __str__(self):
        return str(self.__dict__)