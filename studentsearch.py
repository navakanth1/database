import sqlite3 as sql
connection = sql.connect("college.db")
getroll = input("enter roll number to search?")
result = connection.execute("select *from student where rollnumbe="+getroll)
for i in result:
    print("id",i[0])
    print("name",i[1])
    print("rollnumber",i[2])


