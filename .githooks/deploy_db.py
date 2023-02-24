import mysql.connector
from mysql.connector import Error

if __name__=="__main__":
    import sys  
    try:
        connection = mysql.connector.connect(host=sys.argv[1], 
                                            user=sys.argv[3],
                                            password=sys.argv[4]) 
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("drop database if exists "+ sys.argv[2])
            cursor.execute("create database "+sys.argv[2])
            print("Mysql database for this branch has been reset successfully")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

