import sqlite3
connec =sqlite3.connect('activityschedule.db')
#connec.execute("CREATE TABLE todo(ID INTEGER PRIMARY KEY, ACTIVITY CHAR(200) NOT NULL, STATUS BOOL NOT NULL)")
#status where 1 is bool to mean = Done and 0 = Pending
connec.execute("INSERT INTO todo  VALUES (1,'study online',1)")
connec.execute("INSERT INTO todo  VALUES (2,'study php',0)")
connec.execute("INSERT INTO todo  VALUES (3,'Go visit sweetheart',0)")
connec.execute("INSERT INTO todo  VALUES (4,'enterview with prosper kapp',1)")
connec.execute("SELECT * FROM todo")
ret= connec.execute("SELECT * FROM todo")
print(ret)