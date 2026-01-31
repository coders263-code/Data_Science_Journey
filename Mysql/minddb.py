import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saadi1212",
    database="test1"
)

mycursor = mydb.cursor()

# ❗ QUERY EXECUTE KARNA ZAROORI HAI
#mycursor.execute("SHOW DATABASES")
mycursor.execute("select * from students")


for x in mycursor:
    print(x)

mycursor.close()
mydb.close()