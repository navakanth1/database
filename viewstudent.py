import sqlite3 as sql
connection = sql.connect("college.db")
result = connection.execute("select *from student")
for i in result:
    print("id",i[0])
    print("name",i[1])
    print("rollnumber",i[2])


