# import mysql.connector
# import xlrd
# import pandas as pd

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="anam@123",
#   database="save_info"
# )

# mycursor=mydb.cursor()

# # mycursor.execute("CREATE TABLE person (id int primary key,name varchar(20),age int(5),email varchar(30))")
# loc=("C:\\Users\\ANAM\\Desktop\\python\\Book1.xlsx")

# a=xlrd.open_workbook(loc)
# sheet=a.sheet_by_index(0)
# sheet.cell_value(0,0)

# for i in range(1,6):
#     print(sheet.row_values(i))

# mydb.close()

import csv
with open('Book1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['id'], row['name'],row['age'],row['email'])
