# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
(city TEXT, state TEXT, population INT)""")

# close the databe connection
conn.close()

# conn = sqlite3.connect("cars.db")
# cursor = conn.cursor()
# cursor.execute("""CREATE TABLE inventory
# (make TEXT, model TEXT, quantity INT)""")
# conn.close()
