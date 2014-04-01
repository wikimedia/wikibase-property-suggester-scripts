import argparse
import sys
import time

from propertyimporter.Importer import Importer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program converts wikidata XML dumps to CSV data.")
    parser.add_argument("sourceApiUrl", help="The url of the mediawiki api to copy from", default="http://www.wikidata.org/w/", nargs="?")
    parser.add_argument("destinationApiUrl", help="The url of the mediawiki api to paste to", default="http://localhost/devrepo/w/", nargs="?")
    args = parser.parse_args()

    start = time.time()

    i = Importer()
    i.importProperties(args.sourceApiUrl, args.destinationApiUrl)

    print "total time: %.2fs"%(time.time() - start)