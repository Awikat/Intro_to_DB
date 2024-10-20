import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="salah",
  password="1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

print("Database 'alx_book_store' created successfully!")

"except mysql.connector.Error"
