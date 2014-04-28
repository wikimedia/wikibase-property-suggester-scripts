import argparse
import sys
import time

from valuesuggester.StatementWithItemValueAnalyzer import StatementWithItemValueAnalyzer
from propertysuggester.parser import CsvReader
from propertysuggester.utils.CompressedFileType import CompressedFileType

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program extracts statements wich have an item value. Writes it to <prefix>statement_occurrences.data and <prefix>statement_pair_occurrences.data")
    parser.add_argument("input", help="The input file (lines: <itemId>,<property>,<type>,<value>)", default="StatementsWithItemValue.csv")
    parser.add_argument("prefix", help="The prefix for output files (default=sys.stdout)", default="")
    args = parser.parse_args()

    start = time.time()
    print "extracting statements"

    analyzer = StatementWithItemValueAnalyzer()
    analyzer.analyze(args.input, args.prefix)

    print "done - {0:.2f}s".format(time.time()-start)