#!/usr/bin/python3
"""
This Module conatins a script that lists
all cities from the database hbtn_0e_4_usa
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
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    ORDER BY cities.id"""
    cur.execute(query)

    states_data = cur.fetchall()
    for data in states_data:
        print(data)

    cur.close()
    db_connect.close()
