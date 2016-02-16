# import the sqlite3 library
import sqlite3

conn = sqlite3.connect("newnum.db")

cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop until user enters a valid operation number [1-5]
while True:
    # get user input
    x = raw_input(prompt)

    # if user enter any chioce from 1-4
    if x in set(["1", "2", "3", "4"]):
        # parse the corresponding operation text
        operation = {1:"avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

        # retrieve data
        cursor.execute("SELECT {}(num) from numbers".format(operation))

        get = cursor.fetchone()

        print operation + ": %f" % get[0]

    elif x == "5":
        print "Exit"
        break
