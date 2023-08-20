import connect as c

# create a function
def delete_data():
    # use primary key to delete a record
    idField = input("Enter the FilmID of the records to be deleted: ")

    # DELETE FROM tblfilms WHERE filmID = 1/2/3/4/...
    c.dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField}")
    c.dbCon.commit()
    print(f"Record {idField} deleted from the tblfilms table.")
if __name__ == "__main__":
    delete_data()