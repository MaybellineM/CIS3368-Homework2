import mysql.connector
import creds
from mysql.connector import Error
from sql import Create_connection
from sql import execute_query
from sql import execute_read_query
import flask
from flask import jsonify #function that turns python object to jyson 
from flask import request


#Create a connection to mysql database

myCreds = creds.Creds()
conn = Create_connection(myCreds.conString,myCreds.userName,myCreds.password,myCreds.dbname)

# ADDING A ROW TO MY DATABASE AND EXECTUING QUERY 
tire_brand = 'Corsa'
tire_model = 'Highway Terrain Plus'
tire_loadrating = 115
tire_speedrating = 'up to 112 mph'
tire_type = 'all-season tire'
tire_stock = 8


query = "INSERT INTO Inventory(brand, model, loadrating, speedrating, tiretype, stock) VALUES (%s, %s, %s, %s, %s, %s)"
values = (tire_brand, tire_model, tire_loadrating, tire_speedrating, tire_type, tire_stock)

# Execute the query
#execute_query(conn, query, values)Commented out because I already ran the query




#API Side of the assignment
app = flask.Flask(__name__) #Sets up the application , name of the backend server

#GET method to return  all tires from inventory
@app.route('/api/alltires', methods = ["GET"])
def api_all_tires():
    myCreds = creds.Creds()
    conn = Create_connection (myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbname)

    sql = "SELECT * FROM Inventory"

    tires = execute_read_query(conn,sql)

    conn.close()
    return jsonify(tires)


#POST: This API should allow to add a new tire to inventory

@app.route('/api/addtire', methods = ["POST"])

def addnew_tire():
    #Establish Connection
    myCreds = creds.Creds()
    conn = Create_connection (myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbname)
    
    #Extract values
    new_tire = request.get_json()  
    brand = new_tire['brand']
    model = new_tire['model']
    loadrating = new_tire['loadrating']
    speedrating = new_tire['speedrating']
    tiretype = new_tire['tiretype']
    stock = new_tire['stock']

    new_query = "INSERT INTO Inventory(brand, model, loadrating, speedrating, tiretype, stock) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (brand,model,loadrating,speedrating,tiretype,stock)


    new_tire = execute_query(conn, new_query, values)

    conn.close()
    return jsonify(new_tire)




#PUT: This API should allow to update the stock column of a tire, provided a given id

@app.route('/api/updatestock', methods = ["PUT"])
def update_onhand():
    #Establish connection
    myCreds = creds.Creds()
    conn = Create_connection (myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbname)



    # Extract values
    update_stocks = request.get_json() 
    id = int(update_stocks['id'])
    stock = int(update_stocks['stock'])

    #QUERY for mysql
    stock_query = "UPDATE Inventory SET stock = %s WHERE id = %s"
    stock_values = (stock, id)


    try:
        update_stocks = execute_query(conn, stock_query, stock_values)
    except Exception as e:
        print("Error executing query:", e)

    conn.close()
    return jsonify(update_stocks)




#DELETE: This API should allow to delete a tire, provided a given id









app.run()
'''

 C I T A T I O N S 
https://www.discounttire.com
https://www.geeksforgeeks.org/put-method-python-requests/?ref=header_search
https://realpython.com/api-integration-in-python/#put
'''