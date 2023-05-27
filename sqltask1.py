import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anam@123",
  database="student_details"
)

mycursor=mydb.cursor()

# mycursor.execute("CREATE TABLE stud (id INT PRIMARY KEY ,name VARCHAR(100), age int(10) , email VARCHAR(100))")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

while True:
    choice=int(input("1->Insert Data\n2->Update data\n3->delete data\n4->Show data\n5->Exit\nEnter Choice:"))

    if choice==1:
            try:
                id=int(input("enter id:"))
                name=input("enter name: ")
                age=int(input("enter age:"))
                email=input("enter email:")
                sql="INSERT INTO stud VALUES({},'{}',{},'{}')".format(id,name,age,email)
                mycursor.execute(sql)
                mydb.commit()
                print("record inserted")
            except ValueError:
                print("enter valid input")

    elif choice==2:
        up=int(input("1->update name\n2->Update age\n3->update email\nEnter Choice for updating: "))

        if up==1:
            try:
                id=int(input("enter id"))
                name=input("enter name:")

                sql="UPDATE stud SET name='{}' WHERE id={}".format(name,id)
                mycursor.execute(sql)
                mydb.commit()
                print("name updated")
            except ValueError:
                print("enter valid input")

        elif up==2:
            try:
                id=int(input("enter id"))
                age=int(input("enter age:"))

                sql="UPDATE stud SET age={} WHERE id={}".format(age,id)
                mycursor.execute(sql)
                mydb.commit()
                print("age updated")
            except ValueError:
                print("enter valid input")

        elif up==3:
            try:
                id=int(input("enter id"))
                email=input("enter email:")

                sql="UPDATE stud SET email='{}' WHERE id={}".format(email,id)
                mycursor.execute(sql)
                mydb.commit()
                print("email updated")
            except ValueError:
                print("enter valid input")

    elif choice==3:
        try:
            id=int(input("enter id too delete:"))
            sql="DELETE FROM stud where id={}".format(id)
            mycursor.execute(sql)
            mydb.commit()
            print("record updated")
        except ValueError:
                print("enter valid input")


    elif choice==4:
        mycursor.execute("SELECT * FROM stud")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    elif choice==5:
        break
