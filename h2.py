import mysql.connector
import creds
from mysql.connector import Error
from sql import Create_connection
from sql import execute_query
from sql import execute_read_query


#Create a connection to mysql database

myCreds = creds.Creds()
conn = Create_connection(myCreds.conString,myCreds.userName,myCreds.password,myCreds.dbname)

