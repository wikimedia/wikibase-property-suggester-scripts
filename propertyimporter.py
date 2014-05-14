import argparse
import time

from propertyimporter.Importer import Importer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program inserts entities from source api to target api.")
    parser.add_argument("sourceUrl", help="The url of the mediawiki api to copy from. (default: http://www.wikidata.org/w/api.php)",
                        default="http://www.wikidata.org/w/api.php", nargs="?", type=str)
    parser.add_argument("destinationUrl", help="The url of the mediawiki api to paste to", type=str)
    parser.add_argument("--start", help="At which id to start (default=1)", nargs="?", type=int, default=1)
    parser.add_argument("--end", help="At which id to end (default=1400)", nargs="?", type=int, default=1400)
    parser.add_argument("--loaditems", help="Load Items (default are properties)", action="store_true")
    parser.add_argument("--writejustdummies", help="Override all entities with dummy entries", action="store_true")
    args = parser.parse_args()

    entitytype = "items" if args.loaditems else "properties"
    print "Importing {0} from {1} to {2}".format(entitytype, args.start, args.end)
    print "source: {0}".format(args.sourceUrl)
    print "destination: {0}".format(args.destinationUrl)
    start = time.time()

    importer = Importer(args.sourceUrl, args.destinationUrl, args.loaditems, args.writejustdummies)
    importer.import_entities(args.start, args.end)

    print "total time: %.2fs"%(time.time() - start)
