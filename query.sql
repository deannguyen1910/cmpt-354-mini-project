/
SELECT c.CompetitionID, c.Title
FROM Competitions c
JOIN Proposals p ON c.CompetitionID = p.CompetitionID
WHERE MONTH(c.ApplicationDeadline) = USER_SPECIFIED_MONTH
  AND c.Status = 'Open'
  AND (p.RequestedAmount > 20000 OR (SELECT COUNT(*) FROM Participants WHERE ProposalID = p.ProposalID) > 10)
GROUP BY c.CompetitionID, c.Title
HAVING COUNT(p.ProposalID) >= 1;
/
/
SELECT ProposalID, MAX(RequestedAmount) as LargestRequestedAmount
FROM Proposals p
JOIN Competitions c ON p.CompetitionID = c.CompetitionID
WHERE c.Area = USER_SPECIFIED_AREA
GROUP BY ProposalID
ORDER BY LargestRequestedAmount DESC
LIMIT 1;
/
/
SELECT ProposalID, AwardedAmount
FROM Proposals
WHERE Date < USER_SPECIFIED_DATE
ORDER BY AwardedAmount DESC
LIMIT 1;
/
/
SELECT c.Area, AVG(ABS(p.RequestedAmount - p.AwardedAmount)) as AverageDiscrepancy
FROM Proposals p
JOIN Competitions c ON p.CompetitionID = c.CompetitionID
WHERE c.Area = USER_SPECIFIED_AREA
GROUP BY c.Area;
/
/
SELECT r.ReviewerID
FROM Reviewers r
LEFT JOIN Assignments a ON r.ReviewerID = a.ReviewerID AND a.ProposalID = USER_SPECIFIED_PROPOSAL_ID
LEFT JOIN ConflictOfInterest coi ON r.ReviewerID = coi.ReviewerID AND coi.ConflictedResearcherID = (SELECT PrincipalInvestigator FROM Proposals WHERE ProposalID = USER_SPECIFIED_PROPOSAL_ID)
WHERE coi.ReviewerID IS NULL
GROUP BY r.ReviewerID
HAVING COUNT(a.AssignmentID) < 3;
/
/
SELECT p.ProposalID
FROM Proposals p
JOIN Assignments a ON p.ProposalID = a.ProposalID
JOIN Reviewers r ON a.ReviewerID = r.ReviewerID
JOIN Researchers res ON r.ResearcherID = res.ResearcherID
WHERE CONCAT(res.FirstName, ' ', res.LastName) = USER_SPECIFIED_NAME
AND a.ReviewSubmitted = FALSE;
/