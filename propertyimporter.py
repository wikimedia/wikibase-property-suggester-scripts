import argparse
import sys
import time

from propertyimporter.Importer import Importer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program converts wikidata XML dumps to CSV data.")
    parser.add_argument("sourceUrl", help="The url of the mediawiki to copy from. (default: http://www.wikidata.org/w/)",
                        default="http://www.wikidata.org/w/", nargs="?", type=str)
    parser.add_argument("destinationUrl", help="The url of the mediawiki to paste to", type=str)
    parser.add_argument("--start", help="At which id to start (default=1)", nargs="?", type=int, default=1)
    parser.add_argument("--end", help="At which id to end (default=1200)", nargs="?", type=int, default=1400)
    args = parser.parse_args()


    print "Importing properties from {0} to {1}".format(args.start, args.end)
    print "source: {0}".format(args.sourceUrl)
    print "destination: {0}".format(args.destinationUrl)
    start = time.time()

    importer = Importer(args.sourceUrl, args.destinationUrl, args.start, args.end)
    importer.import_properties()

    print "total time: %.2fs"%(time.time() - start)