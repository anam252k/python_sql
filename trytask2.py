import csv
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anam@123",
    database="save_info"
)
cursor = conn.cursor()
with open('Book1.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Skip header row if necessary

    for row in csv_data:
        # Assuming your CSV columns are in the order: name, age, email
        id=row[0]
        name = row[1]
        age = row[2]
        email = row[3]

        # Prepare and execute the SQL query
        sql = "INSERT INTO person (id,name, age, email) VALUES (%s,%s, %s, %s)"
        data = (id,name, age, email)
        cursor.execute(sql, data)

conn.commit()
cursor.close()
conn.close()
