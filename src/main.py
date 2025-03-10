import argparse
from pubmed.pubmed import fetch
from utils.util import write_to_csv
import pdb

def parse():
    parser = argparse.ArgumentParser(description="a simple cli to fetch research papers based on user query")
    subparsers = parser.add_subparsers(dest="command", required=True)

    
    papers_parser = subparsers.add_parser("papers", help="fetch research papers based on query upto max results")

    papers_parser.add_argument("-f", "--file", help="Enter file name")
    papers_parser.add_argument("-q", "--query", help="Enter query", required=True)
    papers_parser.add_argument("-m", "--max", type=int, help="Max number of results")
    papers_parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")

    args  = parser.parse_args()
    command = args.command
    if command == 'papers':
        file = args.file
        max = args.max
        query = args.query
        if args.debug: pdb.set_trace()
        fetch(query=query, max=max, fileName=file)
          
parse()
