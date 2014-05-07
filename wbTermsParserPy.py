import re
import argparse
from propertysuggester.utils.CompressedFileType import CompressedFileType

if __name__ == "__main__":
   
    parser = argparse.ArgumentParser(description="this program generates a Edit-Item-Suggestions-Table")
    parser.add_argument("input", help="The 'sql wb_terms' input file", type=CompressedFileType('r'))
    args = parser.parse_args()

    for line in args.input:
    	#(?:'en'|'de'|'fr')
        for text in re.findall(r"\(([^,']*,[^,']*,'[^,']*','en','[^,']*','[^,']*','[^,']*',[^,']*)\)", line):
            print text
            