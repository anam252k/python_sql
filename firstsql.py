import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anam@123",
  database="mydatabase"
)

mycursor=mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

# sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
# val = [('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)

# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


# mycursor.execute("SELECT * FROM customer")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql="UPDATE customer SET name='abc' WHERE name='ben'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# sql="DELETE FROM customer WHERE name='abc'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")