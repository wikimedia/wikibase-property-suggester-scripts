
from collections import defaultdict



def compute_table(generator, classifier_ids=(31, 106)):
    """
    @type generator: collections.Iterable[Entity]
    @return: dict[int, dict]
    """
    table = defaultdict(lambda: defaultdict(int))

    for i, entity in enumerate(generator):
        if i % 100000 == 0 and i > 0:
            print "entities {0}".format(i)

        distinct_ids = set(claim.property_id for claim in entity.claims)

        for pid1 in distinct_ids:
            if pid1 in classifier_ids:
                continue
            tuple = (pid1, None)
            table[tuple]["appearances"] += 1
            for pid2 in distinct_ids:
                if pid1 != pid2:
                    table[tuple][pid2] += 1

        classifier = [claim for claim in entity.claims if claim.property_id in classifier_ids and claim.datatype == "wikibase-entityid"]

        for claim in classifier:
            tuple = (claim.property_id, int(claim.value[1:]))
            table[tuple]["appearances"] += 1
            for pid2 in distinct_ids:
                if claim.property_id != pid2:
                    table[tuple][pid2] += 1
    return table

