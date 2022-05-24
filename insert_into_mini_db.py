from pickle import FROZENSET
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Add code here to insert a new record
sql = "INSERT INTO `person` (`first_name`, `last_name`, `age`, `email`) VALUES (%s, %s, %s, %s)"


"INSERT INTO courier(name,number) VALUES('John David',07495965011),('David Malki',07495965022),('Daniel James',07495965033),('Pritchard Smite',0749596544),('Calleb Green',07495960055)"
;

'''SELECT FROM Miniproject

sql=''INSERT INTO products('name','price') VALUES('coke',1.00),('Latte',1.4),('Hot Chocolate',1.6),('Latte',1.4),('Coffee',2.0),('smoothie',1.3)

cursor.execute?

cursor.execute(sql, ('Jane', 'Doe', 20, 'jane_doe@invalidemail.com'))

'''
connection.commit()
cursor.close()
connection.close()