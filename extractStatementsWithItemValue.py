import argparse
import sys
import time

from valuesuggester.StatementWithItemValueExtractor import StatementWithItemValueExtractor
from propertysuggester.parser import CsvReader
from propertysuggester.utils.CompressedFileType import CompressedFileType

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program extracts statements wich have an item value")
    parser.add_argument("input", help="The input file (lines: <item>,<property>,<type>,<value>)", type=CompressedFileType('r'))
    parser.add_argument("output", help="The output file (default=sys.stdout)", default="StatementsWithItemValue.csv")
    args = parser.parse_args()

    start = time.time()
    print "extracting statements"

    extractor = StatementWithItemValueExtractor()
    extractor.extract(CsvReader.read_csv(args.input), args.output)

    print "done - {0:.2f}s".format(time.time()-start)