import logging

from propertysuggester.utils.WikidataApi import WikidataApi

logging.basicConfig(format='%(levelname)s:%(message)s')

class Importer:
    def __init__(self, source_url, destination_url, start, end, loaditems):
        self.source_api = WikidataApi(source_url)
        self.destination_api = WikidataApi(destination_url)
        self.start = start
        self.end = end
        self.type = "item" if loaditems else "property"
        self.idtemplate = "Q{0}" if loaditems else "P{0}"

    def import_entities(self):
        for numericId in xrange(self.start, self.end):
            if numericId % 10 == 0:
                print "{0}/{1}".format(numericId, self.end)
            else:
                print ".",
            entityid = self.idtemplate.format(numericId)

            try:
                self.clone_entity(entityid)
            except Exception, e:
                logging.error("failed while cloning {0}".format(entityid), str(e))

    def clone_entity(self, entityid):
        source_json = self.source_api.get_entity_by_id(entityid)
        destination_json = self.destination_api.get_entity_by_id(entityid)
        if source_json:
            if not destination_json:
                self.destination_api.create_entity(self.build_data(source_json), self.type)
            else:
                self.destination_api.overwrite_entity(self.build_data(source_json), entityid)
        else:
            dummy = {"labels": {"en-gb": {"language": "en-gb", "value": "dummy" + entityid}},
                     "descriptions": {"en-gb": {"language": "en-gb", "value": "Propertydescription"}},
                     "datatype": "string"}
            if not destination_json:
                try:
                    self.destination_api.create_entity(dummy, self.type)
                except Exception, e:
                    logging.warning("fail to create dummy {0}".format(entityid))
            else:
                self.destination_api.overwrite_entity(dummy, entityid)

    def check_lengthconstrains(self, prop, entity_json):
        lengthconstrained = ["descriptions", "labels"]
        multilang_limits = 250  # from options.wiki

        if prop in lengthconstrained:
            for k, v in entity_json[prop].items():
                if len(v['value'].encode("utf-8")) >= multilang_limits:
                    logging.debug(u'Warning "{entity} - {prop} - {lang}: {value}" violates length constrains'.format(
                        entity=entity_json["title"], prop=prop, lang=k, value=v['value']
                    ))
                    del entity_json[prop][k]

    def remove_claim_ids(self, entity_json):
        for claim in entity_json["claims"].values():
            for snak in claim:
                del snak["id"]

    def build_data(self, entity_json):
        props = ["aliases", "labels", "descriptions", "datatype", "claims"]
        data = {}

        for prop in props:
            if prop in entity_json:
                self.check_lengthconstrains(prop, entity_json)
                data[prop] = entity_json[prop]

        if "claims" in data:
            self.remove_claim_ids(data)

        return data