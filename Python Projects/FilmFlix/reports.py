import connect as c

def reportAll():
    c.dbCursor.execute("SELECT * FROM tblFilms")
    print(c.dbCursor.fetchall())

if __name__ == "__main__":
    reportAll()

def reportGenre():
    genreNeed = input("Enter a genre: ").title()
    c.dbCursor.execute("SELECT * FROM tblFilms WHERE Genre = ?", (genreNeed,))
    print(c.dbCursor.fetchall())

if __name__ == "__main__":
    reportGenre()
    
def reportYear():
    yearNeed = input("Enter a year: ")
    c.dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (yearNeed,))
    print(c.dbCursor.fetchall())
    
if __name__ == "__main__":
    reportYear()

def reportRating():
    ratingNeed = input("Enter a Rating: ")
    c.dbCursor.execute("SELECT * FROM tblFilms WHERE Rating = ?", (ratingNeed,))
    print(c.dbCursor.fetchall())

if __name__ == "__main__":
    reportRating()


