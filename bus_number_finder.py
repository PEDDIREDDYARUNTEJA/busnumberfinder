import sqlite3 as sql
print("-----------welcome to hyderabad busroute and number finder-------")
con=sql.connect('hyderabad_busroute_database')
curs=con.cursor()
startpoint=input("enter startpoint :").upper()
endpoint=input("enter endpoint :").upper()
k="select * from busroute"
curs.execute(k)
data=curs.fetchall()
if len(data)>0:
    for i in data:
        if startpoint in i[1] and endpoint in i[1]:
            print(i[0])
            k=i[1].split()
            for j in k:
                print(k)
else:
    print("there is no direct bus for your search")    
con.close()