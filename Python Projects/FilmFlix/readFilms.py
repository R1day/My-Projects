import connect as c
 
# Create a function to read records in the songs table
def read_data():

    # select all record in the songs table
    c.dbCursor.execute("SELECT * FROM tblfilms")

    # fetch the selected songs using the fetchall() method
    allRecords = c.dbCursor.fetchall()

    # loop through the fetched records and display each in the terminal
    for eachRecord in allRecords:
        # and display each in the terminal
        print(eachRecord)



if __name__ == "__main__":
    read_data()