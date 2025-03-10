import requests
from .parser import parse_json, parse_pubmed_xml
from utils.util import write_to_csv
def fetch(query : str, max:int = 10, fileName : str=None):
    base_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    search_url = f"{base_url}/esearch.fcgi?db=pubmed&term={query.replace(' ', '+')}&retmode=json&retmax={max}&usehistory=y"
    response = requests.get(search_url)
    (webenv, queryKey) = parse_json(response)
    fetch_url = f"{base_url}/efetch.fcgi?db=pubmed&query_key={queryKey}&WebEnv={webenv}&retmax=2"
    response = requests.get(fetch_url)
    parsed_data = parse_pubmed_xml(response.content)
    write_to_csv(fileName, data=parsed_data)



