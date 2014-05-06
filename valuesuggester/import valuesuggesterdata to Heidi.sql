DROP TABLE IF EXISTS vs_statement_occurrences ;
CREATE TABLE vs_statement_occurrences
(
propertyId int,
valueEntityId int, 
occurrences int
)
;

LOAD DATA INFILE "C:/Bachelorprojekt/Repositories/PropertySuggester-PythonValues/dumps/processed/vs_statement_occurrences.data"
INTO TABLE vs_statement_occurrences
FIELDS
	TERMINATED BY ','
;

CREATE INDEX statement_id_pair 
ON vs_statement_occurrences (propertyId, valueEntityId);

DROP TABLE IF EXISTS vs_statement_pair_occurrences;
CREATE TABLE vs_statement_pair_occurrences
(
s1Id int,
s1ValueId int, 
s2Id int,
s2ValueId int, 
occurrences int
)
;

LOAD DATA INFILE "C:/Bachelorprojekt/Repositories/PropertySuggester-PythonValues/dumps/processed/vs_statement_pair_occurrences.data"
INTO TABLE vs_statement_pair_occurrences
FIELDS
	TERMINATED BY ','
;

CREATE INDEX statement_pair_id_pair 
ON vs_statement_pair_occurrences (s1Id, s1ValueId, s2Id);