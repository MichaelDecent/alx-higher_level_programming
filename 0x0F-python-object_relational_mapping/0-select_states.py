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

    cu = db_connect.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cu.execute(query)

    states_data = cu.fetchall()
    for row in states_data:
        print(row)

    cu.close()
    db_connect.close()
