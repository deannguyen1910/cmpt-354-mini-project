import sqlite3
conn = sqlite3.connect('council.db')

# myFavArtist = input("Enter your favorite artist's name: ")

cursor = conn.cursor()
print("Opened database successfully \n")

with conn:
    cur = conn.cursor()

    # task1 = "SELECT c.CompetitionID, c.Title FROM Competitions c JOIN Proposals p ON c.CompetitionID = p.CompetitionID WHERE MONTH(c.ApplicationDeadline) = USER_SPECIFIED_MONTH AND c.Status = 'Open' AND (p.RequestedAmount > 20000 OR (SELECT COUNT(*) FROM Participants WHERE ProposalID = p.ProposalID) > 10) GROUP BY c.CompetitionID, c.Title HAVING COUNT(p.ProposalID) >= 1;"
    # task2 ="SELECT ProposalID, MAX(RequestedAmount) as LargestRequestedAmount FROM Proposals p JOIN Competitions c ON p.CompetitionID = c.CompetitionID WHERE c.Area = USER_SPECIFIED_AREA GROUP BY ProposalID ORDER BY LargestRequestedAmount DESC LIMIT 1;"
    # task3 = "SELECT ProposalID, AwardedAmount FROM Proposals WHERE Date < USER_SPECIFIED_DATE ORDER BY AwardedAmount DESC LIMIT 1;"
    # task4= "SELECT c.Area, AVG(ABS(p.RequestedAmount - p.AwardedAmount)) as AverageDiscrepancy FROM Proposals p JOIN Competitions c ON p.CompetitionID = c.CompetitionID WHERE c.Area = USER_SPECIFIED_AREA GROUP BY c.Area;"
    # task5= "SELECT r.ReviewerID FROM Reviewers r LEFT JOIN Assignments a ON r.ReviewerID = a.ReviewerID AND a.ProposalID = USER_SPECIFIED_PROPOSAL_ID LEFT JOIN ConflictOfInterest coi ON r.ReviewerID = coi.ReviewerID AND coi.ConflictedResearcherID = (SELECT PrincipalInvestigator FROM Proposals WHERE ProposalID = USER_SPECIFIED_PROPOSAL_ID) WHERE coi.ReviewerID IS NULL GROUP BY r.ReviewerID HAVING COUNT(a.AssignmentID) < 3;"
    # task6= "SELECT p.ProposalID FROM Proposals p JOIN Assignments a ON p.ProposalID = a.ProposalID JOIN Reviewers r ON a.ReviewerID = r.ReviewerID JOIN Researchers res ON r.ResearcherID = res.ResearcherID WHERE CONCAT(res.FirstName, ' ', res.LastName) = USER_SPECIFIED_NAME AND a.ReviewSubmitted = FALSE;"
    
    myQuery = "SELECT * FROM Researchers"

    ## create the 
    cur.execute(myQuery)
    # cur.execute(myQuery,{"myArtist":myFavArtist})

    rows=cur.fetchall()
    # if rows: -
        # print("We do have the following albums from your favorite artist, " + myFavArtist + ": ")
    # else:
        # print("Unfortunately, we do not have any albums by " + myFavArtist + "!\n")

    for row in rows:
        print(row)
    print("\n")


if conn:
    conn.close()
    print("Closed database successfully")