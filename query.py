import sqlite3
conn = sqlite3.connect('council.db')

cursor = conn.cursor()
print("Opened database successfully \n")
# Area = "Biology"
# Date = "2024-10-10"
# FirstName = "Emily"
# LastName = "Young"
# Proposal = 0
Area = None
Date = None
FirstName = None
LastName = None
Proposal = None

while (True):
    print ("1. Find all competitions (calls for grant proposals) open at a user-specified month, which already have at least one submitted large proposal. For a proposal to be large, it has to request more than $20,000 or to have more than 10 participants, including the principle investigator. Return both IDs and the titles.")
    print("2. For a user-specified area,  find the proposal(s) that request(s) the largest amount of money.")
    print("3. For a user-specified date,  find the proposals submitted before that date that are awarded the largest amount of money.")
    print ("4. For an area specified by the user, output its average requested/awarded discrepancy, that is, the absolute value of the difference between the amounts.")
    print ("5. Reviewer assignment: Provide the user with the option of assigning a set of reviewers to review a specific grant application (research proposal), one proposal at a time. The proposal ID should be specified by the user. Before doing the reviewers assignment, the user should be able to request and receive a list of reviewers who are not in conflict with the proposal being reviewed, and who still have not reached the maximum of three proposals to review.")
    print ("6: For a user-specified name,  find the proposal(s) he/she needs to review.")
    print ("0. Exit")
    value = int(input('Input your choice: '))
    
    if (value == 0):
        break

    with conn:
        cur = conn.cursor()
        if (value == 1):
            task1 = " SELECT c.CompetitionID, c.Title FROM Competitions c INNER JOIN ( SELECT CompetitionID FROM Applications WHERE (ApplicationID IN ( SELECT ApplicationID FROM ( SELECT ApplicationID, COUNT(*) AS participants FROM workOn GROUP BY ApplicationID ) WHERE participants >= 10 ) OR RequestedAmount >= 20000 ) ) AS a ON c.CompetitionID = a.CompetitionID WHERE strftime('%m', SubmittedDate) < '12';  "
            cur.execute(task1)

        if (value == 2):
            Area = None
            Area = (input('Input area: '))
            task2 = " SELECT * FROM Applications JOIN Competitions ON Competitions.CompetitionID = Applications.CompetitionID WHERE Competitions.Area = '%%%%%%%%';  "
            cur.execute(task2.replace("%%%%%%%%", Area))

        if (value == 3):
            Date = None
            task3 = " SELECT Applications.*  FROM Applications WHERE AwardedAmount = ( SELECT MAX(Applications.AwardedAmount)  FROM Applications JOIN Competitions ON Applications.CompetitionID = Competitions.CompetitionID WHERE Competitions.SubmittedDate < '%%%%%%%%' );  "
            Date = (input('Input date: '))
            cur.execute(task3.replace("%%%%%%%%", Date))

        if (value == 4):
            Area = None
            Area = (input('Input area: '))
            task4 = " SELECT AVG(ABS(AwardedAmount - RequestedAmount)) FROM Applications  WHERE Applications.CompetitionID = ( SELECT CompetitionID FROM Competitions WHERE Area = '%%%%%%%%')"
            cur.execute(task4.replace("%%%%%%%%", Area))
        
        if (value == 5):
            task5_1 = " SELECT * FROM Applications WHERE ApplicationID IN ( SELECT ApplicationID FROM Review GROUP BY ApplicationID HAVING COUNT(DISTINCT ReviewID) < 3 )  " ## check application is still need
            cur.execute(task5_1)
            applications=cur.fetchall()
            for application in applications:
                print("applicationID:", application[0], application)
            Proposal = None
            Proposal = int(input('Choose applicationID: '))
            ReviewID = None
            for application in applications:
                a0, a1, a2, a3, a4, a5, a6 = application
                if int(a0) == Proposal:
                    ReviewID = a5 
            task5_2 = " SELECT * FROM Researchers WHERE Organization NOT IN ( SELECT Organization FROM Researchers  WHERE ResearcherID IN ( SELECT R1.ReviewID FROM Review R1 JOIN Review R2 ON R1.ApplicationID = R2.ApplicationID WHERE R2.ReviewID = %%%%%%%% ) )  " ## not in the same university the working on get from proposal
            cur.execute(task5_2.replace(("%%%%%%%%"), str(ReviewID)))
            lists1=cur.fetchall()

            
            task5_3 = "  SELECT A.Deadline FROM Applications A JOIN Review R ON A.ApplicationID = R.ApplicationID WHERE R.ReviewID IN ( SELECT R1.ReviewID FROM Review R1 JOIN Review R2 ON R1.ApplicationID = R2.ApplicationID WHERE R2.ReviewID = %%%%%%%% AND R1.ReviewID != R2.ReviewID)    " # last work together... replace with principle of proposal
            cur.execute(task5_3.replace(("%%%%%%%%"), str(ReviewID)))
            lists2=cur.fetchall()
           
            list = []
            for item in lists1:
                if item not in lists2:
                    list.append(item)
            for item in list:
                print(item)
            AddReviewID = int(input('Choose reviewID: ')) 
            task5_4 = "INSERT INTO Review (ApplicationID, ReviewID) VALUES (F%%%%%%%%, L%%%%%%%%);"
            cur.execute(task5_4.replace(("F%%%%%%%%"), str(Proposal)).replace(("L%%%%%%%%"), str(AddReviewID)))
            cur.fetchall()
            continue
        if (value == 6):
            FirstName = None
            FirstName = (input('Input First name: '))
            LastName = None
            LastName = (input('Input Last name: '))
            task6 = " SELECT * FROM Applications WHERE ApplicationID == ( SELECT ApplicationID FROM Review WHERE Review.ReviewID == ( SELECT Researchers.ResearcherID FROM Researchers WHERE Researchers.FirstName == 'F%%%%%%%%' AND Researchers.LastName ==  'L%%%%%%%%' ) )  "
            cur.execute(task6.replace("F%%%%%%%%", FirstName).replace("L%%%%%%%%", LastName))
    


        
    
        task5_3 = "  SELECT A.Deadline FROM Applications A JOIN Review R ON A.ApplicationID = R.ApplicationID WHERE R.ReviewID IN ( SELECT R1.ReviewID FROM Review R1 JOIN Review R2 ON R1.ApplicationID = R2.ApplicationID WHERE R2.ReviewID = %%%%%%%% AND R1.ReviewID != R2.ReviewID)    " # last work together... replace with principle of proposal



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