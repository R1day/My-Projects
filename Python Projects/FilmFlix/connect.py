import sqlite3 as sql # import the sqlite3 module and assign it with an alias (sql)

# to use the sqlite3(sql) module: Create a DB connection object(variable)
"bdCon is a variable that is assigned everything on the right(sql.connect()"
dbCon = sql.connect("filmflix.db") # sqlite3(sql).connect() = create or open (if one exist) a DB

# Create a cursor object(variable) and pass/assign it to the cursor method
dbCursor = dbCon.cursor()