import connect as c
c.dbCursor.execute(""" 
CREATE TABLE "tblfilms" (
	"FilmID"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"yearReleased"	INTEGER,
	"Rating"	TEXT,
    "Duration" INTEGER,
    "Genre" TEXT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)""")