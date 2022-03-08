import sqlite3 as sql


connection = sql.connect("product.db")
# connection.execute('''  create table productdata(
#                           productcode integer primary key autoincrement,
#                           productname text,
#                           productprice integer,
#                           distributorname text
#
#
#
#
#
#
#
#
# );     ''')
print("Table created successfully")
getproductcode = input("Enter productcode:")
getproductname = input("Enter productname:")
getproductprice = input("Enter productprice:")
getdistributorname = input("Enter distributorname:")
connection.execute("Insert table productdata(productcode, productname, productprice, distributorname) \
values("+getproductcode+",'"+getproductname+"',"+getproductprice+",'"+getdistributorname+"')")

connection.commit()
connection.close()
print("inserted sucessfully")