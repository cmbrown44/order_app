# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

import db


def viewAllRecords():
    query = "SELECT * FROM orders"
    data = db.runQuery(query)
    return data

def enterOrder(customer_name, drink_type, drink_size, extras, price):
    query = f"INSERT INTO orders (customer_name, drink_type, drink_size, extras, price) VALUES ('{customer_name}', '{drink_type}', '{drink_size}', '{extras}', {price})"
    db.runQuery(query)
    return "Order received :)"

def readID(order_id):
    query = f"SELECT * FROM orders WHERE order_id = {order_id};"
    return db.runQuery(query)

def updateOrder(order_id, customer_name, drink_type, drink_size, extras, price):
    update_query = f"UPDATE orders SET customer_name = '{customer_name}', drink_size = '{drink_size}', drink_type = '{drink_type}', \
        extras = '{extras}', price = '{price}'  WHERE order_id = {order_id};"
    db.runQuery(update_query)
    return True

def removeOrder(order_id):
    remove_str = f"DELETE FROM orders WHERE order_id = {order_id}"
    db.runQuery(remove_str)
    return True

def deleteOrders():
    delete_str = "DELETE * FROM orders"
    db.runQuery(delete_str)
    return True

def updateDB():
    return db.commitChanges()
    

print(viewAllRecords())