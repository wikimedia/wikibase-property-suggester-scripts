[![Build Status](https://travis-ci.org/Wikidata-lib/PropertySuggester-Python.png?branch=master)](https://travis-ci.org/Wikidata-lib/PropertySuggester-Python)
[![Coverage Status](https://coveralls.io/repos/Wikidata-lib/PropertySuggester-Python/badge.png?branch=master)](https://coveralls.io/r/Wikidata-lib/PropertySuggester-Python)

# PropertySuggester Scripts
Contains scripts for PropertySuggester to preprocess the wikidata dump

## Install
Run the command:
```
sudo apt-get install build-essential python-pip python-dev
python setup.py install
```
## Usage 
- use dumpconverter.py to convert a wikidata dump to csv
- use analyzer.py to create a csv file with the suggestion data that can be loaded into a sql table
- the PropertySuggester extension provides a maintenance script (maintenance/UpdateTable.php) that allows to load the csv into the database

```
python scripts/dumpconverter.py wikidatawiki-20140226-pages-articles.xml.bz2 dump.csv
python scripts/analyzer.py dump.csv wbs_propertypairs.csv
php extensions/PropertySuggester/maintenance/UpdateTable.php --file wbs_propertypairs.csv
```

### Run tests
```
pytest .
```

## Release Notes

### 3.0.0
* Restructure repository
* Using pytest instead of nosetests

### 2.0.0
* Consider classifying Properties
* use Json dumps for analysis

### 1.1
* Generate associationrules for qualifier and references
* Improve ranking to avoid suggestions of human properties
* remove very unlikely rules (<1%)

### 1.0
* Converts a wikidata dump to a csv file with associationrules between properties
