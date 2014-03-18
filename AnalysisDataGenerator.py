from collections import defaultdict

deprecatedProperties = [107, 76, 71, 77, 70, 57, 74, 168]

def computeTable(generator):
    """
    @type generator: collections.Iterable[Entity]
    @return: dict[int, dict], dict[String, list]
    """
    i = 0
    table = {}
    entities = {}
    for entity in generator:
        entities[entity.title] = []
        i+=1
        if i%1000000 == 0:
            print str(i) + " items analyzed"
        for claim in entity.claims:
            pid = claim.property_id
            if claim.datatype == "wikibase-entityid" and pid not in deprecatedProperties:   #classes are represented by wikibase-entities
                if not pid in table:
                    table[pid] = defaultdict(int)
                if not pid in entities[entity.title]:  
                    table[pid]["appearances"] += 1   #count occurences for each property
                    entities[entity.title].append(pid)
                if not claim.value in table[pid]:  #for each property keep track of occuring values and entities described by specific property,value combinations
                    table[pid][claim.value] = []
                table[pid][claim.value].append(entity.title) #specific (entity, property, value) - triple can only occur once - so no need to check for existance here
    return table, entities

