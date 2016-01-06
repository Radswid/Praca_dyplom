# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
import sys

con = None
uwykonana = False
try:
    con = psycopg2.connect(database='psw',user='postgres',password='1234')
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('SELECT * FROM psw_commands WHERE wykonana=%(wykonana)s', {'wykonana':uwykonana})
    rows = cursor.fetchall()
    for row in rows:
        
        print ("%s %s %s %s %s" % (row['id'], row['ip'], row['system'], row['ram'],row['quote']))

except psycopg2.DatabaseError as e:
    print ('Error %s' %e)
    sys.exit(1)

finally:
    if con:
        con.close()
