#!/usr/bin/python3
"""
This Module contains  a script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
    query = """SELECT cities.name
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""
    cur.execute(query, (argv[4],))

    cities_data = cur.fetchall()
    print(", ".join([data[0] for data in cities_data]))

    cur.close()
    db_connect.close()
