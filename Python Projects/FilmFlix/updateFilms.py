import connect as c

# create a function
def update_data():
    # use primary key to update a record
    idField = input("Enter the filmID of the records to be updates: ")

    # field to be updated: Title, YearReleased, Rating, Duration, Genre
    
    titleField = input("Enter Title value: ").title()
    yearReleasedField = input("Enter yearReleased: ").title()
    ratingField = input("Enter film Rating from PG, R, and G: ")
    durationField = input("Enter film Duration in minutes: ")
    genreField = input("Enter film Genre: ").title()

    # field value: ask for the value for the field(Title, YearReleased, Genre) to be updated
    titleField = "'"+titleField+"'"
    yearReleasedField = "'"+yearReleasedField+"'"
    ratingField = "'"+ratingField+"'" 
    durationField = "'"+durationField+"'"
    genreField = "'"+genreField+"'"  

    # update a record in the songs table
    "UPDATE songs SET Title or YearReleased or Rating or Duration or Genre = TitleValue or YearReleasedValue or RatingValue or DurationValue or GenreValue WHERE filmID = 1/2/3/4..."
    c.dbCursor.execute(f"UPDATE tblfilms SET Title = {titleField}, YearReleased = {yearReleasedField}, Rating = {ratingField}, Duration = {durationField}, Genre = {genreField} WHERE filmID = {idField}")
    c.dbCon.commit()
    print(f"Record {idField} update in the tblfilms table.")
if __name__ == "__main__":
    update_data() # Call or invoke the subroutine or function