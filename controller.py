# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to 
# query and create data and will return the data back to the user

import service

print(
    """
    Welcome to the QA Cafe, what would you like to do? 

    1. Create an order
    2. Read an order
    3. Read all Orders
    4. Update an order
    5. Delete an order
    6. Delete all orders
    """
)

print(service.viewAllRecords())