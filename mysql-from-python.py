import os
import pymysql

# (modify this variable if running on another environment)
username = 'root'

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')


# Return results as a dictionary
try:
    # Run a query - if create an argument to return dictionary use cursors argument pymysql.cursors.DictCursor
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        # sql = "SELECT * FROM Artist;"
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
        # result = cursor.fetchall()
        # print(result)

finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
