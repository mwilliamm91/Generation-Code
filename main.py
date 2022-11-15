import csv
import os
# ***********************variables***********************
products = ["coke","fanta","water"]
all_orders = []
order_status = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]

# ******** functions**************

# imports customer orders and appends the orders to all_orders

def import_orders():
    try:
        with open("./orders.csv", "r") as file:
            contents = csv.DictReader(file)
            for row in contents:
                all_orders.append(row)
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
      
    new_customer_orders.append({"Customer_name": customer_name, "Customer_address":customer_address, "Customer_phone_number": customer_phone_number, "Status": "pending"})
 
# writes the orders in a separate file (orders.csv)    
def writes_orders(new_orders):
    try:
        orders_file = "./orders.csv"
        if os.path.isfile(orders_file):
            with open("./orders.csv", "a", newline="") as file:
                fieldnames = ["Customer_name", "Customer_address", "Customer_phone_number", "Status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for new_order in new_orders:
                    writer.writerow(new_order)
                    new_orders.remove(new_order)
        else:
            with open(orders_file, "w", newline="") as file:
                fieldnames = ["Customer_name", "Customer_address", "Customer_phone_number", "Status"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for new_order in new_orders:
                    writer.writerow(new_order)
                    new_orders.remove(new_order)      
    except IOError:
        print("I/O error")

        
# displays indexed customer orders
def indexed_orders():
    for ind, val in enumerate(all_orders):
        print(ind, ":", val )
       

def changes_order_status(order_index, status_index):
    if order_index in range(len(all_orders)):
        if status_index in range(len(order_status)):
            current_order_status = all_orders[order_index]['Status']
            all_orders[order_index]["status"]= order_status[status_index]
            print(f"Order status has been changed from {current_order_status} to {order_status[status_index]}\n")
            print(all_orders[order_index])
    else:
        print("Incorrect input or out of range")

def changes_key_value_properties(order_index):
    if order_index not in range(len(all_orders)) and order_index == '':
         print("No property has been changed")
    else:
        print("\n", all_orders[order_index], "\n")
        for key in all_orders[order_index].keys():
            while True:
                user_input= input(f"Would you like to change {key}? Enter Y for yes or N for no. \n").title()
                if user_input != "N" and user_input != "Y":
                    print("Invalid input")
                    break
                elif user_input == "N":
                    print(f"{key} wasn't changed")
                    break
                else:
                    value_input = input(f"Enter the new {key} \n")
                    all_orders[order_index].update({key:value_input})
                    print(f"{key}:{value_input}")
                    break
        orders_file = "./orders.csv"
        with open(orders_file, "w", newline="") as file:
            fieldnames = ["Customer_name", "Customer_address", "Customer_phone_number", "Status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_orders)

# **************deletes an order from an indexed list given the index and updates the txt file*********************

def deletes_order(order_index):
    if order_index in range(len(all_orders)):
        all_orders.remove(all_orders[order_index])
    orders_file = "./orders.csv"
    with open(orders_file, "w", newline="") as file:
        fieldnames = ["Customer_name", "Customer_address", "Customer_phone_number", "Status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_orders)
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
                print(f"There are {len(all_orders)} orders")
                if len(all_orders) == 0:
                    pass
                else:
                    print(f"Orders are shown below: \n{all_orders}")
                continue
            elif order_menu_options == 2:
                customer_details_input()
                writes_orders(new_customer_orders) 
                continue
            elif order_menu_options == 3:
                indexed_orders()
                order_index_input = int(input("Enter the order index to proceed \n"))
                
                for (index, value) in enumerate(order_status):
                    print(index, ":", value)
                order_status_input = int(input("Enter the chosen order status index as displayed above \n"))
                changes_order_status(order_index_input,order_status_input)               
                continue
            elif order_menu_options == 4:
                indexed_orders()
                selected_input = int(input("Enter the index to update \n"))
                changes_key_value_properties(selected_input)
                continue
            elif order_menu_options == 5:
                indexed_orders()
                selected_input = int(input("Enter the index to delete\n"))
                deletes_order(selected_input)  
            else:
                print("Enter a valid input")
            

    
 
        
        
     
 


 



