import csv
import os
# ***********************variables***********************
all_products = []
all_orders = []
all_couriers = []
order_status = ["Preparing", "Awaiting Pickup", "Out for Delivery", "Delivered"]

                       # ******** functions**************

# ***************main app function*****************
def displays_main_menu():
    print('''
        0. Quit the app
        1. Show product menu
        2. Show the courier menu
        3. Show order menu \n 
          ''')
# ****************Product menu display*******************
def displays_product_menu():
    print("""-----PRODUCTS-----
    0. Return to main menu
    1. View all products
    2. Add a new Product
    3. Update Product
    4. Delete Product
---------------------""")

#  ***************Order menu display**********************
def displays_order_menu():
    print('''-----ORDERS-----
    0. Return to main menu
    1. View all orders
    2. Add a new order
    3. Update an order's status
    4. Update an order
    5. Remove an order
---------------------''')

# **************Courier menu display***********************

def displays_courier_menu():
    print('''------Couriers-------
          0: Return to main menu
          1: View all couriers 
          2: Add a new courier
          3: Update an existing courier
          4: Delete a courier from the list
-----------------------''')


# ********** adds new orders into a list ***************
new_customer_orders = []

def customer_details_input():
    customer_name = input("Enter the customer's name\n")
    customer_address = input("Enter the customer's address\n")
    customer_phone_number = input("Enter the customer's phone number\n")
    indexed_items(all_products)
    user_order_input = input("\nEnter the index of products you want to add separated by commas.\n")
    indexed_items(all_couriers)
    user_courier_input = int(input("\nEnter the index of the courier.\n"))
    # appending to the temp new_customer_order list
    new_customer_orders.append({"Customer_name": customer_name, "Customer_address":customer_address, "Customer_phone_number": customer_phone_number, "Courier":user_courier_input, "Status": "Preparing", "Items": user_order_input})
 
# ************writes the orders in a separate file (orders.csv)*************
def writes_orders(new_orders):
    try:
        orders_file = "./orders.csv"
        if os.path.isfile(orders_file):
            with open(orders_file, "a", newline="") as file:
                fieldnames = ["Customer_name", "Customer_address", "Customer_phone_number", "Courier", "Status","Items"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for new_order in new_orders:
                    writer.writerow(new_order)
                    new_orders.remove(new_order)
        else:
            with open(orders_file, "w", newline="") as file:
                fieldnames = ["Customer_name", "Customer_address", "Customer_phone_number", "Courier", "Status","Items"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for new_order in new_orders:
                    writer.writerow(new_order)
                    new_orders.remove(new_order)
    except IOError:
        print("I/O error")

        
# *****************displays indexed items************************
def indexed_items(list):
    for ind, val in enumerate(list):
        print(f"{ind}: {val}")
       
# ********** changes the order status of an order when passed the order's index*********************
def changes_order_status(order_index, status_index):
    if order_index in range(len(all_orders)):
        if status_index in range(len(order_status)):
            current_order_status = all_orders[order_index]['Status']
            all_orders[order_index]["status"]= order_status[status_index]
            print(f"Order status has been changed from {current_order_status} to {order_status[status_index]}\n")
            print(all_orders[order_index])
    else:
        print("Incorrect input or out of range")
# ********** loops through the key, value pair and changes the value if user requests and saves into a csv file*****************

def changes_key_value(order_index, list_file, link, field_names):
    if order_index not in range(len(list_file)) and order_index == '':
        print("No property has been changed")
    else:
        print("\n", list_file[order_index], "\n")
        for key in list_file[order_index].keys():
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
                    list_file[order_index].update({key:value_input})
                    print(f"The {key} has been changed to {value_input}\n")
                    break
        with open(link, "w", newline="") as file:
            headers = field_names
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(list_file)

# *******deletes an order from an indexed list given the index and updates the csv file*********************

def deletes_order(order_index, delete_from_file, link, field_names):
    try:
        if order_index in range(len(delete_from_file)):
            delete_from_file.remove(delete_from_file[order_index])
        with open(link, "w", newline="") as file:
            headers = field_names
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(delete_from_file)
    except FileNotFoundError as fnfe:
        print(f"{fnfe}: error encountered")
    except:
        print("Ooops! something went wrong. Please try again.")

       
# Adds a new courier and saves to a list and text file
new_couriers = []
def adds_courier(couriers):
    new_courier = {}
    new_courier_name = input("Enter the new courier's name.\n")
    new_courier_phone = int(input("Enter the courier's phone number. \n"))
    new_courier.update(Name=new_courier_name, Phone_number = new_courier_phone)
    couriers.append(new_courier)
    
# **************writes to couriers.txt*************
    try:
        couriers_file = "./couriers.csv"
        if os.path.isfile(couriers_file):
            with open(couriers_file, "a", newline="") as file:
                fieldnames = ["Name", "Phone_number"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for courier in couriers:
                    writer.writerow(courier)
                    couriers.remove(courier)
        else:
            with open(couriers_file, "w", newline="") as file:
                fieldnames = ["Name", "Phone_number"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for courier in couriers:
                    writer.writerow(courier)
                    couriers.remove(courier)      
    except IOError:
        print("I/O error")
    
# **************adds a new product and writes it a a csv file********
new_products = []
def add_new_product(products):
    try:
        products_file = "./products.csv"
        if os.path.isfile(products_file):
            with open(products_file, "a", newline="") as file:
                fieldnames = ["Name", "Price"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for product in products:
                    writer.writerow(product)
                    products.remove(product)
        else:
            with open(products_file, "w", newline="") as file:
                fieldnames = ["Name", "Price"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for product in products:
                    writer.writerow(product)
                    products.remove(product)      
    except IOError:
        print("I/O error")
        
# ***********import files (orders, products, couriers) ****************

def import_files(link, container):
    try:
        with open(link, "r", newline="") as file:
            contents = csv.DictReader(file)
            for content in contents:
                container.append(content)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        


# *********************welcome message*******************

print("\n Welcome to the app \n")

# ******************Main app section**********************

while True:
    import_files("./orders.csv", all_orders)
    import_files("./products.csv", all_products)
    import_files("./couriers.csv", all_couriers)
    displays_main_menu()
    #  GET user input for main menu option
    start_app_input = int(input("Select input as shown above \n"))
    # check for valid input
    if start_app_input != 0 and start_app_input != 1 and start_app_input != 2 and start_app_input != 3:
        print(">>>>> Error: Invalid input")
        continue
    elif start_app_input == 0:
    # quits app if the user select 0
        print("quitting the app")
        break
    elif start_app_input == 1:
    # input selections for the product menu
        while True: 
            displays_product_menu()  
        
            product_menu_options = int(input("Select input as shown above \n"))
            
            # returns different outputs depending on user selection
            
            if product_menu_options == 0 :
                print("....returning to main menu")
                break
            elif product_menu_options == 1:
                print(f"\n There are {len(all_products)} products as shown below:\n")
                for prod in all_products:
                    print(prod)
                continue
            elif product_menu_options == 2:
                product_name = input("\nEnter the name of the product to add \n")
                product_price = float(input("\nEnter the all_products's price \n"))
                new_product = {}
                new_product.update(Name= product_name, Price=product_price)
                new_products.append(new_product)
                print(f"added {product_name} to the product list.")
                # saving new product in a csv file
                add_new_product(new_products)
                continue
            elif product_menu_options == 3:
                indexed_items(all_products)
                item_to_update = int(input("Enter index of product to update"))
                changes_key_value(item_to_update, all_products, "./products.csv", ["Name", "Price"])
                continue
            elif product_menu_options == 4:
                print("\n")
                indexed_items(all_products)
                item_to_delete = int(input("\nEnter index of item to delete \n"))
                deletes_order(item_to_delete, all_products, "./products.csv", ["Name", "Price"])
                print("Product has been deleted")
                continue
            else:
                print("Invalid option selected \n")
                continue
        
    elif start_app_input == 2:
        while True:
            displays_courier_menu()
            
            courier_menu_options = int(input("Select an input as shown above \n"))
            if courier_menu_options == 0:
                print("....returning to main menu \n")
                break
            elif courier_menu_options == 1:
                print(f"There are {len(all_couriers)} couriers as shown below:\n")
                for courier in all_couriers:
                    print(courier)
                continue
            elif courier_menu_options == 2:
                adds_courier(new_couriers)
                continue
            elif courier_menu_options == 3:
                indexed_items(all_couriers)
                courier_index_input = int(input("\n Enter the index to update an existing courier \n"))
                changes_key_value(courier_index_input, all_couriers, "./couriers.csv", ["Name", "Phone_number"])
                continue
            elif courier_menu_options == 4:
                indexed_items(all_couriers)
                courier_index_input = int(input("\n Enter the index to delete an existing courier \n"))
                deletes_order(courier_index_input, all_couriers, "./couriers.csv", ["Name", "Phone_number"])
                print("Courier has been deleted")   
                continue
            else:
                print("Enter a valid input!")
                
    elif start_app_input == 3:
        while True:
            displays_order_menu()
            
            order_menu_options = int(input("Select input as shown above \n"))
            
            if order_menu_options == 0:
                print("....returning to main menu \n")
                break
            elif order_menu_options == 1:
                if len(all_orders) == 0:
                    pass
                elif len(all_orders) < 2:
                    print(f"There is {len(all_orders)} order as shown below:\n")
                    for order in all_orders:
                       print(order)
                    print("\n")
                else:
                    print(f"There are {len(all_orders)} orders as shown below:\n")
                    for order in all_orders:
                       print(order)
                continue
            elif order_menu_options == 2:
                customer_details_input()
                writes_orders(new_customer_orders)
                continue
            elif order_menu_options == 3:
                indexed_items(all_orders)
                order_index_input = int(input("Enter the order index to proceed \n")) 
                indexed_items(order_status)
                order_status_input = int(input("Enter the chosen order status index as displayed above \n"))
                changes_order_status(order_index_input,order_status_input)               
                continue
            elif order_menu_options == 4:
                indexed_items(all_orders)
                selected_input = int(input("Enter the index to update \n"))
                changes_key_value(selected_input, all_orders, "./orders.csv", ["Customer_name", "Customer_address", "Customer_phone_number", "Courier", "Status","Items"])
                continue
            elif order_menu_options == 5:
                indexed_items(all_orders)
                selected_input = int(input("Enter the index to delete\n"))
                deletes_order(selected_input, all_orders, "./orders.csv", ["Customer_name", "Customer_address", "Customer_phone_number", "Courier", "Status","Items"])
                continue
            else:
                print("Enter a valid input")
                break
            

    
 
        
        
     
 


 



