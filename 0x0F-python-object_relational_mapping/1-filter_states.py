#!/usr/bin/python3
"""
This Module contains a script that lists all states with
a name starting with N (upper N) from the database hbtn_0e_0_usa

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
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(query)

    states_data = cur.fetchall()
    for data in states_data:
        if data[1][0] == 'N':
            print(data)

    cur.close()
    db_connect.close()
