import connect as c # import the connect.py module

# create a function
def insert_data():
    # Note: film ID is set to autoincrement, input/data is not required
    filmTitle = input("Enter the film Title: ").title()
    filmYearReleased = input("Enter yearReleased: ").title()
    filmRating = input("Enter film Rating from PG, R, and G: ")
    filmDuration = input("Enter film Duration in minutes: ")
    filmGenre = input("Enter film Genre: ").title()

    c.dbCursor.execute("INSERT INTO tblfilms(Title, YearReleased, Rating, Duration, Genre) VALUES(?,?,?,?,?)",(filmTitle, filmYearReleased, filmRating, filmDuration, filmGenre))
    
    c.dbCon.commit() # permanently write this record to the table in the database

    print(f"{filmTitle} Insert in the films table")

if __name__ == "__main__": 
    insert_data()


c.dbCursor.execute("INSERT INTO tblfilms (Title, YearReleased, Rating, Duration, Genre) VALUES ('Spider-Man: Across the Spider-Verse', 2023, 'PG', 140, 'Science fiction')")