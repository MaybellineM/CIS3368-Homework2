import mysql.connector
from mysql.connector import Error

def Create_connection(host_name,user_name,user_pw, db_name):
    connection= None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_pw,
            db = db_name

        )
        print("connection to MYSQL Successful")
    except Error as e:
        print(f"The error'{e}' has occured")
    return connection


def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


        
def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
         print(f"The error'{e}' has occured")