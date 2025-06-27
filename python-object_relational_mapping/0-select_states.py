#!/usr/bin/env python3
import MySQLdb
import sys

def main():
    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
