import argparse
import sys
import time

from propertyimporter.Importer import Importer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program converts wikidata XML dumps to CSV data.")
    parser.add_argument("sourceUrl", help="The url of the mediawiki to copy from. (default: http://www.wikidata.org/w/)", default="http://www.wikidata.org/w/", nargs="?")
    parser.add_argument("destinationUrl", help="The url of the mediawiki to paste to")
    args = parser.parse_args()

    start = time.time()

    importer = Importer()
    importer.importProperties(args.sourceUrl, args.destinationUrl)

    print "total time: %.2fs"%(time.time() - start)