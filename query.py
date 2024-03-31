import sqlite3
conn = sqlite3.connect('council.db')

# myFavArtist = input("Enter your favorite artist's name: ")

cursor = conn.cursor()
print("Opened database successfully \n")

with conn:
    cur = conn.cursor()

    myQuery = "SELECT * FROM albums NATURAL JOIN artists WHERE Name=:myArtist"

    # cur.execute(myQuery,{"myArtist":myFavArtist})

    rows=cur.fetchall()
    # if rows:
        # print("We do have the following albums from your favorite artist, " + myFavArtist + ": ")
    # else:
        # print("Unfortunately, we do not have any albums by " + myFavArtist + "!\n")

    for row in rows:
        print(row[1])
    print("\n")


if conn:
    conn.close()
    print("Closed database successfully")