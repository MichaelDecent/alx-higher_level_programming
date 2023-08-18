#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db_connect = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db_connect.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)

    states_data = cur.fetchall()
    for row in states_data:
        print(row)

    cur.close()
    db_connect.close()
