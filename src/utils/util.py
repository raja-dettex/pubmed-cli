import csv
from pathlib import Path
from typing import List, Dict
import os
def write_to_csv(name: str = None, data: List[Dict[str,any]] = None):
    if data is None:
        return
    fileName = f"{name}.csv"  if name else 'papers.csv'
    filePath = Path(__file__).resolve().parent.parent.parent.parent.joinpath(f"output")
    os.makedirs(filePath, exist_ok=True)
    with open(f"{filePath}/{fileName}", 'w', newline='') as file:
        headers = { 'PubmedID', 'Title', 'Publication Date', 'Non-Academic Author(s)', 'Company Affiliation(s)', 'Corresponding Author Email'}
        csv_writer = csv.DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(data)