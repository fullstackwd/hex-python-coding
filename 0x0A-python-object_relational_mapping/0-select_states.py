#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Check that the correct number of arguments have been passed
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)
        
    # Try to connect to the database
    try:
        db = MySQLdb.connect(
            host="localhost", 
            user=sys.argv[1], 
            port=3306, 
            passwd=sys.argv[2], 
            db=sys.argv[3])
    except MySQLdb.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)
    
    # Get a cursor object and execute the query
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM states")
    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")
        sys.exit(1)
    
    # Retrieve the results and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Close the database connection
    db.close()
