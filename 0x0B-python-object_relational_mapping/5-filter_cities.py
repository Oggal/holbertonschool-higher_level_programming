#!/usr/bin/python3
'''Get All States, requires User, Password, Database'''
import MySQLdb
import sys


def filter_states():
    '''Get Cites and States from sql table'''
    if(len(sys.argv) < 5):
        print(sys.argv)
        return
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    try:
        db = MySQLdb.connect(
            "localhost",
            mysql_username,
            mysql_password,
            database_name)
    except Exception as e:
        return (0)
    target = sys.argv[4]
    target = target.split('"')[0]
    target = target.split("'")[0]
    cursor = db.cursor()
    cursor.execute(
        "SELECT \
        (SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM\
        cities WHERE cities.state_id =states.id), id\
        FROM states WHERE states.name = '{}';".format(target))
    rows = cursor.fetchall()
    for r in rows:
        print(r[0])
    cursor.close()
    db.close()


if __name__ == '__main__':
    filter_states()
