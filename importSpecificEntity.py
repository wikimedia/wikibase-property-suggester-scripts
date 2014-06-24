__author__ = 'felix.niemeyer'

import argparse
import time

from propertyimporter.Importer import Importer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program inserts one specific entity from source api to target api")
    parser.add_argument("sourceUrl", help="The url of the mediawiki api to copy from. (default: http://www.wikidata.org/w/api.php)",
                        default="http://www.wikidata.org/w/api.php", nargs="?", type=str)
    parser.add_argument("destinationUrl", help="The url of the mediawiki api to paste to", type=str)
    parser.add_argument("eId", help="The numeric id of the target entity", type=str)
    parser.add_argument("eType", help="The type of the target entity [property|item]", default="item" )
    args = parser.parse_args()
    prefix = "P" if args.eType == "property" else "Q"

    print "Importing {0} {1}".format(args.eType, args.eId)
    print "source: {0}".format(args.sourceUrl)
    print "destination: {0}".format(args.destinationUrl)
    start = time.time()

    importer = Importer(args.sourceUrl, args.destinationUrl, ("item" == args.eType) )
    importer.clone_entity(prefix + args.eId)

    print "total time: %.2fs"%(time.time() - start)