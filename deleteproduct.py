import sqlite3 as sql
connection = sql.connect("product.db")
getproductname = input("enter productname to be deleted?")
connection.execute("delete from student where productname="+getproductname)
connection.commit()
print("deleted successfully")
result = connection.execute("select * from product")
for i in result:

    print("productcode",i[0])
    print("productname",i[1])
    print("distributorname",i[2])

