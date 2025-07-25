# given the `books.csv` dataset
# create an sqlite database (open a connection)
# create a table (get the cursor and execute)
#
# the columns are Title	Author	Genre	Pages	Publisher

# and insert all data with cursor.executemany()
#
# don't forget to commit.
# 
# then run a select query
# and iterate over the result, printing it.

#######################################################################
# next level: normalize the dataset, by creating the following tables #
#      authors, publishers, genres, books                             #
#######################################################################


import sqlite3
import csv
conn = sqlite3.connect(r"C:\Users\UA38IV\OneDrive - ING\Desktop\Python training\books.db")
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE BOOKS(ID INTEGER PRIMARY KEY, TITLE TEXT, AUTHOR TEXT, GENRE TEXT, PAGES INTEGER, PUBLISHER TEXT)")
except sqlite3.OperationalError:
    # this means the table already exists
    pass
else:
    # we just created the table, let's populate the data
    with open(r"C:\Users\UA38IV\OneDrive - ING\Desktop\Python training\python-intermediate\docs\books.csv") as file_in:
        book_list = csv.reader(file_in) 
        #next to consume the header line
        next(book_list)
        cur.executemany("insert into BOOKS(TITLE, AUTHOR, GENRE, PAGES, PUBLISHER) VALUES (?, ?, ?, ?, ?)", book_list)
        conn.commit()
res = cur.execute('Select * from BOOKS')
for row in res:
    print(row)