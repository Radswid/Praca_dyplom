# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import sys

con = None
try:
    con = psycopg2.connect(database='psw',user='postgres',password='1234')
    cur = con.cursor()
    cur.execute('SELECT * FROM psw_commands WHERE ')
    rows = cur.fetchall()
    for row in rows:
        print (row)

except psycopg2.DatabaseError as e:
    print ('Error %s' %e)
    sys.exit(1)

finally:
    if con:
        con.close()
