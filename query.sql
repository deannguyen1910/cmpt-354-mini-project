/
SELECT c.CompetitionID, c.Title
FROM Competitions c
INNER JOIN (
SELECT CompetitionID
FROM Applications
WHERE (ApplicationID IN (
SELECT ApplicationID
FROM (
SELECT ApplicationID, COUNT(*) AS participants
FROM workOn
GROUP BY ApplicationID
)
WHERE participants >= 10
)
OR RequestedAmount >= 20000
)
) AS a
ON c.CompetitionID = a.CompetitionID
WHERE strftime('%m', SubmittedDate) < '12';
/