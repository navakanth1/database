import sqlite3 as sql
connection = sql.connect("college.db")
getroll = input("enter roll number to be deleted?")
connection.execute("delete from student where rollnumber="+getroll)
connection.commit()
print("deleted successfully")
result = connection.execute("select * from student")
for i in result:

    print("id",i[0])
    print("name",i[1])
    print("rollnumber",i[2])


