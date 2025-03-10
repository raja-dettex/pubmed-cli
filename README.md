# Research Paper Fetcher CLI

## Description
A Python CLI program to fetch research papers based on a user-specified query. The program identifies papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results as a CSV file.

## Installation
Ensure you have Python installed (version 3.x recommended). This project uses [Poetry](https://python-poetry.org/) for dependency management. To set up the environment, run:

```sh
poetry install
```

## Usage
```sh
poetry run python src/main.py [-h] {papers} ...
```

### **Positional Arguments**
- `{papers}`
  - `papers` → Fetch research papers based on the query (up to a max number of results).

### **Required Arguments**
- `--query` → Pass a search string for fetching papers. If the string contains spaces, wrap it in quotes (`''`).

### **Optional Arguments**
- `--file` → Specify the output CSV file name.
- `--max` → Set the maximum number of research papers to fetch.

### **Debugging Mode**
- `--debug` or `-d` → Enable debugging mode using Python's `pdb` utility (default is `False`).

### **Help**
```sh
poetry run python src/main.py --help
```
This will display:
```
usage: main.py [-h] {papers} ...

a simple cli to fetch research papers based on user query

positional arguments:
  {papers}
    papers    fetch research papers based on query up to max results

options:
  -h, --help  show this help message and exit
```
```

## Example Commands
### **Fetch Papers with a Query**
```sh
poetry run python main.py papers --query 'cancer research' --max 10 --file results
```

### **Enable Debugging Mode**
```sh
poetry run python src/main.py papers --query 'machine learning in biotech' -d
```

## License
MIT License

