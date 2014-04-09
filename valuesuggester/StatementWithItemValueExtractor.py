from collections import defaultdict

from StatementWithItemValueFile import StatementWithItemValueFile

class StatementWithItemValueExtractor:

    def extract(self, generator, outFile):
        """
        @type generator: collections.Iterable[Entity]
        @return: dict[int, dict]
        """
        outFs = StatementWithItemValueFile(outFile, "write")

        table = defaultdict()
        for i, entity in enumerate(generator):
            entityId = entity.title
            if i % 100000 == 0 and i > 0:
                print "processed {0} items".format(i)
            for claim in entity.claims:
                if claim.datatype == "wikibase-entityid" : 
                    outFs.writeStatement(int(entityId[1:]), claim.property_id, int(claim.value[1:]))

