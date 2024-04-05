/
SELECT * FROM Applications
WHERE ApplicationID == (
SELECT ApplicationID FROM Review
WHERE Review.ReviewID == (
SELECT Researchers.ResearcherID FROM Researchers
WHERE Researchers.FirstName == 'Emily' AND Researchers.LastName ==  'Young'
)
)
/