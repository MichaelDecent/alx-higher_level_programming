#!/usr/bin/python3
"""
This Module contains  a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where name matches
the argument
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
    query = ("""SELECT * FROM states
             WHERE name = '{:s}'
             ORDER BY id ASC""".format(argv[4]))
    cur.execute(query)

    states_data = cur.fetchall()
    for data in states_data:
        if argv[4] in data:
            print(data)

    cur.close()
    db_connect.close()
