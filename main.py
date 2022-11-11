import csv
# ***********************variables***********************
products = ["coke","fanta","water"]
customer_orders = []
order_status = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]

# ******** functions**************

# imports customer orders and appends the orders to customer_orders

def import_orders():
    try:
        with open("./orders.csv", "r") as file:
            contents = csv.DictReader(file)
            for row in contents:
                customer_orders.append(row)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")

import_orders()

# ***************main app function*****************
def main_menu_display():
    print('''
          0. Quit the app
          1. Show product menu
          2. Show order list \n 
          ''')
# ****************Product menu display*******************
def display_product_menu():
    print("""-----PRODUCTS-----
    0. Exit 
    1. View Product List
    2. Add a Product
    3. Update Product
    4. Delete Product
---------------------""")

#  ***************Order menu display**********************
def display_order_menu():
    print('''-----ORDERS-----
        0. Exit
        1. View Order List
        2. Add an order
        3. Update an order's status
        4. Update an order
        5. Remove an order
---------------------''')

# adds new orders into a list

new_customer_orders = []

def customer_details_input():
    customer_name = input("Enter the customer's name")
    customer_address = input("Enter the customer's address")
    customer_phone_number = input("Enter the customer's phone number")
      
    new_customer_orders.append({"customer_name": customer_name, "customer_address":customer_address, "customer_phone_number": customer_phone_number, "status": "pending"})
 
# writes the orders in a separate file (orders.csv)    
def writes_orders(new_orders):
    try:
        with open("./orders.csv", "w") as file:
            fieldnames = ["customer_name", "customer_address", "customer_phone_number", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for order in new_orders:
                writer.writerow(order)
    except IOError:
        print("I/O error")
        
# displays indexed customer orders
def indexed_orders():
    for i in range(len(customer_orders)):
        print(customer_orders.index(i), ":", i)

def changes_order_status(order_index, status_index):
    if order_index in range(len(indexed_orders)):
        if status_index in range(len(order_status)):
            current_order_status = customer_orders[order_index]['status']
            customer_orders[order_index]["status"]= order_status[status_index]
            print(f"Order status has been changed from {current_order_status} to {order_status[status_index]}\n")
            print(customer_orders[order_index])

def changes_key_value_properties(order_index):
    if order_index in range(len(customer_orders)) and order_index != '':
         
        user_input_data = customer_orders[order_index]
        
        
        for key, value in user_input_data.items():
            print(key, value)
        print(customer_orders)
    else:
        print("No property has been changed")
            



# *********************welcome message*******************
print("Welcome to the app \n")

while True:
    
    main_menu_display()
    #  GET user input for main menu option
    start_app_input = int(input("Select input as shown above \n"))
    # check for valid input
    if start_app_input != 0 and start_app_input != 1 and start_app_input != 2:
        print(">>>>> Error: Invalid input")
        continue
    elif start_app_input == 0:
    # quits app if the user select 0
        print("quitting the app")
        break
    elif start_app_input == 1:
    # input selections for the product menu    
        while True: 
            display_product_menu()  
        
            product_menu_options = int(input("Select input as shown above \n"))
            
            # returns different outputs depending on user selection
            
            if product_menu_options == 0 :
                print("....returning to main menu")
                break
            elif product_menu_options == 1:
                print(f"{products}\n")
                print("....returning back to product menu \n")
                continue
            elif product_menu_options == 2:
                added_item = input("Enter the name of the item to add")
                products.append(added_item)
                print(f"added {added_item} to the list. The new list is {products}")
                break
            elif product_menu_options == 3:
                for item in products:
                    print(f"{products.index(item)}: {item}")
                item_to_update = int(input("Enter index of item to update"))
                new_product_name = input("Enter new product name")
                products[item_to_update] = new_product_name
                print("item updated")
                break
            elif product_menu_options == 4:
                for item in products:
                    print(f"{products.index(item)}: {item}")
                item_to_delete = int(input("Enter index of item to delete"))
                products.pop(item_to_delete)
                print("product has been removed")
                break
            else:
                print("Invalid option selected \n")
                continue
        
    elif start_app_input == 2:

        while True:
            display_order_menu()
            
            order_menu_options = int(input("Select input as shown above \n"))
            
            if order_menu_options == 0:
                print("....returning to main menu \n")
                break
            elif order_menu_options == 1:
                print(f"There are {len(customer_orders)} orders")
                if len(customer_orders) == 0:
                    pass
                else:
                    print(f"Orders are shown below: \n{customer_orders}")
                continue
            elif order_menu_options == 2:
                customer_details_input()
                writes_orders(new_customer_orders) 
                continue
            elif order_menu_options == 3:
                indexed_orders()
                order_index_input = int(input("Enter the order index to proceed\n"))
                for i in range(len(order_status)):
                    print(order_status.index(i), ":", i)
                order_status_input = int(input("Enter the chosen order status index as displayed above\n"))
                changes_order_status(order_index_input,order_status_input)               
                continue
            elif order_menu_options == 4:
                indexed_orders()
                selected_input = int(input("Enter the chosen order status index as displayed above\n"))
                changes_key_value_properties(selected_input)
                continue
            else:
                print("Enter a valid input")
            

    
 
        
        
     
 


 



