from requests import Response
from json.decoder import JSONDecodeError
import xml.etree.ElementTree as ET
from typing import Dict, List



def parse_json(res: Response)->  tuple[str]:
    try:
        data = res.json()
        webenv: str = data['esearchresult']['webenv']
        queryKey: str = data['esearchresult']['querykey']
        return (webenv, queryKey)
    except JSONDecodeError as e:
        print("unable to parse, not valid json: " + str(e))
    return (None, None)


def parse_pubmed_xml(xml: str) -> List[Dict[str, any]]:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        print("not a valid xml string: {e}")
        return None
    finally:
        articles: List[Dict[str, any]] = []
        
        for article in root.findall(".//PubmedArticle"):
            pubmed_id = article.find(".//PMID").text if article.find(".//PMID") is not None else None
            
            # Fetch the correct Title (not ArticleTitle)
            title = article.find(".//Journal/Title").text if article.find(".//Journal/Title") is not None else None

            # Extract Publication Date (Year, Month, and Day)
            pub_date_element = article.find(".//PubDate")
            pub_year = pub_date_element.find("Year").text if pub_date_element is not None and pub_date_element.find("Year") is not None else "Unknown"
            pub_month = pub_date_element.find("Month").text if pub_date_element is not None and pub_date_element.find("Month") is not None else "Unknown"
            pub_day = pub_date_element.find("Day").text if pub_date_element is not None and pub_date_element.find("Day") is not None else "Unknown"
            publication_date = f"{pub_year}-{pub_month}-{pub_day}"

            # Extract Non-Academic Authors & Company Affiliations
            non_academic_authors = []
            company_affiliations = []
            for author in article.findall(".//Article/AuthorList/Author"):
                first_name = author.find(".//ForeName").text if author.find(".//ForeName") is not None else None
                last_name = author.find(".//LastName").text if author.find(".//LastName") is not None else None
                if first_name is None and last_name is None:
                    continue
                elif first_name is  None:
                    non_academic_authors.append(last_name)
                    continue
                elif last_name is None:
                    non_academic_authors.append(first_name)
                    continue
                non_academic_authors.append(f"{first_name} {last_name}")
            # Extract Corresponding Author Email
            corresponding_author_email = None
            for affiliation_info in article.findall(".//AffiliationInfo"):
                if affiliation_info is not None and affiliation_info.find("Affiliation") is not None:
                    text = affiliation_info.find("Affiliation").text
                    affiliations = text.split(',')
                    for affiliation in affiliations:
                        if "un" not in affiliation.lower() and "insti" not in affiliation.lower() and '@' not in affiliation.lower():
                            company_affiliations.append(affiliation)
                    if text and "@" in text:
                        corresponding_author_email = text.split()[-1]  # Extract email (assuming it's last in text)
                        break
                
            
            articles.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": publication_date,
                "Non-Academic Author(s)": non_academic_authors,
                "Company Affiliation(s)": company_affiliations,
                "Corresponding Author Email": corresponding_author_email
            })
        
        return articles



