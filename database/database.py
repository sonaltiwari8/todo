import mysql
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    port=3306,
    username="<YOUR_USERNAME>",
    password="<YOUR_PASSWORD>",
    database="todos"
)
