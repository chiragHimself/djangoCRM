import pymysql

# Connect to MySQL using pymysql
dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="ronaldo"
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")

# Close the connection
dataBase.close()
