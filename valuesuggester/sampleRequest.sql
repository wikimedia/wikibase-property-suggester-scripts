/*sample query for vs_statement_pair_occurences usage*/

SELECT 
	/* s1Id, s1ValueId, po1.occurences as po1, s2Id, s2ValueId, po2.occurences as po2, rule.occurences, rule.occurences/po1.occurences */
	rule.s2Id as propertyId,
	s2ValueId as value, 
	rule.occurences as coverage, 
	( 1 - EXP(SUM(LOG(1- ( (rule.occurences*1.0/po.occurences) / (pair_occurence.probability ) ))) ) ) as probability
FROM 
	vs_statement_pair_occurences as rule, vs_statement_occurences as po, wbs_propertypairs as pair_occurence
WHERE
	(s1Id, s1ValueId) IN	((106, 186360), (31,5)) /* Staatsangehörigkeit:Österreich, Gender:male, profession:physiker */
	
	AND pair_occurence.pid1 = s1Id
	AND pair_occurence.pid2 = s2Id
	 
	AND po.propertyId = s1Id 
	AND po.valueEntityId = s1ValueId
	
	
GROUP BY rule.s2Id, rule.s2ValueId
	/*
ORDER BY probability desc*/