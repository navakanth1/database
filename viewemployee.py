import sqlite3 as sql
connection = sql.connect("company.db")
result = connection.execute("select *from employee")
for i in result:
    print("employeeid",i[0])
    print("employeename",i[1])
    print("employeedesignation",i[2])

