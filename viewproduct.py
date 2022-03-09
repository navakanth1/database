import sqlite3 as sql
connection = sql.connect("product.db")
result = connection.execute("select *from productdata")
for i in result:
    print("productcode",i[0])
    print("productname",i[1])
    print("productprice",i[2])


