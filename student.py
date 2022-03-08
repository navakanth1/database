import sqlite3 as sql
connection = sql.connect("college.db")
#connection.execute('''  create table student(
#                          id integer primary key autoincrement,
 #                         name text,
  #                        rollnumber integer,
   #                       admno integer,
    #                      college text
#







#);     ''')
print("table created sucessfully")


getname =input("Enter name:")
getrollnumber =input("Enter rollnumber")
getadmno = input("Enter admno number")
getcollege =input("Enter college")

connection.execute("Insert into student(name, rollnumber, admno, college) \
values('"+getname+"',"+getrollnumber+","+getadmno+",'"+getcollege+"')")
connection.commit()
connection.close()
print("inserted successfully")