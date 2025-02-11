import os
import sqlite3 as sql
con=sql.connect('hyderabad_busroute_database')
curs=con.cursor()
table="create table busroute(BUS_NUMBER varchar(10),BUS_ROUTE varchar(500))"
curs.execute(table)
con.close()