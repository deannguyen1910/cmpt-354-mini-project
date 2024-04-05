import sqlite3
conn = sqlite3.connect('council.db')

# myFavArtist = input("Enter your favorite artist's name: ")

cursor = conn.cursor()
print("Opened database successfully \n")
Area = "Biology"
Date = "2024-10-10"
FirstName = "Emily"
LastName = "Young"
with conn:
    cur = conn.cursor()
    task2 = " SELECT * FROM Applications WHERE Applications.CompetitionID == (     SELECT CompetitionID FROM Competitions     WHERE Competitions.Area == '%%%%%%%%')"
    task3 = " SELECT Applications.*  FROM Applications WHERE AwardedAmount = ( SELECT MAX(Applications.AwardedAmount)  FROM Applications JOIN Competitions ON Applications.CompetitionID = Competitions.CompetitionID WHERE Competitions.Deadline < '%%%%%%%%' );  "
    task4 = " SELECT AVG(ABS(AwardedAmount - RequestedAmount)) FROM Applications  WHERE Applications.CompetitionID = ( SELECT CompetitionID FROM Competitions WHERE Area = '%%%%%%%%')"
    task6 = " SELECT * FROM Applications WHERE ApplicationID == ( SELECT ApplicationID FROM Review WHERE Review.ReviewID == ( SELECT Researchers.ResearcherID FROM Researchers WHERE Researchers.FirstName == 'F%%%%%%%%' AND Researchers.LastName ==  'L%%%%%%%%' ) )  "
    # cur.execute(task2.replace("%%%%%%%%", Area))
    # cur.execute(task3.replace("%%%%%%%%", Date))
    # cur.execute(task4.replace("%%%%%%%%", Area))
    # cur.execute(task6.replace("F%%%%%%%%", FirstName).replace("L%%%%%%%%", LastName))

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