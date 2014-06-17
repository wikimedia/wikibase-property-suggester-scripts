SELECT id,
timestamp,
Convert(session_id,char) as session_id,
convert(entity,char) as entity,
Convert(properties, char) as propertes,
convert(suggestions,char) as suggestions,
convert(missing, char) as missing,
convert(overall, char) as overall,
convert(opinion, char) as opinion
from wbs_evaluations
ORDER BY entity desc;