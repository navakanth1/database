import sqlite3 as sql


connection = sql.connect("company.db")
# connection.execute('''  create table employee(
#                           employeeid integer primary key autoincrement,
#                           employeename text,
#                           employeedesignation text,
#                           employeesalary integer,
#                           companyname text,
#                           mobilennumber integer
#
#
#
# );    ''')
print("table created successfully")
getemployeename = input("Enter employeename")
getemployeedesignation = input("Enter employeedesignation")
getemployeesalary = input("Enter employeesalary")
getcompanyname = input("Enter companyname")

connection.execute("insert into employee(companyname,employeename, employeedesignation, employeesalary) \
values ('"+getemployeename+"', '"+getemployeedesignation+"', "+getemployeesalary+", '"+getcompanyname+"')")
connection.commit()
connection.close()
print("Inserted successfully")