import argparse
import sys
import time

from propertyimporter.Importer import Importer

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program converts wikidata XML dumps to CSV data.")
    parser.add_argument("inApiUrl", help="The url of the mediawiki api to copy from", default="http://www.wikidata.org/w", nargs="?")
    parser.add_argument("outApiUrl", help="The url of the mediawiki api to paste to", default="http://localhost/devrepo/core", nargs="?")
    args = parser.parse_args()

    start = time.time()

    i = Importer()
    i.importProperties(args.inApiUrl, args.outApiUrl)

    print "total time: %.2fs"%(time.time() - start)