SELECT 
	
	rules.s2Id as propertyId,
	rules.s2ValueId as value, 
	( 1 - EXP(SUM(LOG(1- ( (rules.occurrences*1.0/property_value_occurrences.occurrences) / (property_property_occurrences.probability ) ))) ) ) as pr
FROM 
	vs_statement_pair_occurrences as rules, vs_statement_occurrences as property_value_occurrences, wbs_propertypairs as property_property_occurrences
WHERE
	(s1Id, s1ValueId) IN	((31,5))
	
	AND property_property_occurrences.pid1 = s1Id
	AND property_property_occurrences.pid2 = s2Id
	 
	AND property_value_occurrences.propertyId = s1Id 
	AND property_value_occurrences.valueEntityId = s1ValueId
	
	AND rules.s2Id = 509
	
GROUP BY rules.s2Id, rules.s2ValueId
HAVING 
	pr > 0.01
ORDER BY pr desc