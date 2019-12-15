#!/usr/bin/python3
""" lists all states from hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 INNER JOIN states\
                 ON cities.state_id = states.id\
                 WHERE states.name=%s", (sys.argv[4], ))
    rows = cur.fetchall()
    ciu = ""
    for i in rows:
        for j in i:
            ciu += j + ', '
    ciu = ciu[:-2]
    print("{}".format(ciu))
