import mysql.connector
import creds
from mysql.connector import Error
from sql import Create_connection
from sql import execute_query
from sql import execute_read_query


#Create a connection to mysql database

myCreds = creds.Creds()
conn = Create_connection(myCreds.conString,myCreds.userName,myCreds.password,myCreds.dbname)

# ADDING A ROW TO MY DATABASE AND EXECTUING QUERY 
tire_brand = 'Corsa'
tire_model = 'Highway Terrain Plus'
tire_loadrating = 115
tire_speedrating = 'up to 112'
tire_type = 'all-season tire'
tire_stock = 8


query = "INSERT INTO Inventory(brand, model, loadrating, speedrating, tiretype, stock) VALUES (%s, %s, %s, %s, %s, %s)"
values = (tire_brand, tire_model, tire_loadrating, tire_speedrating, tire_type, tire_stock)

# Execute the query
#execute_query(conn, query, values)Commented out because I already ran the query
