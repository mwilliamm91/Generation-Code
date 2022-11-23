import csv
from utils import create_indexed_list


order_status = ["Preparing", "Awaiting Pickup",
                "Out for Delivery", "Delivered"]

# ***************Order menu display**********************


def displays_order_menu():
    """ displays order menu options"""
    print('''-----ORDERS-----
    0. Return to main menu
    1. View all orders
    2. Add a new order
    3. Update an order's status
    4. Update an order
    5. Remove an order
---------------------''')

# ********** adds new orders into a list ***************


def creates_order(product_list, couriers_list):
    """ takes inputs from user and appends to a list"""
    new_customer_orders = []
    customer_name = input("Enter the customer's name\n")
    customer_address = input("Enter the customer's address\n")
    customer_phone_number = input("Enter the customer's phone number\n")

    create_indexed_list(product_list)
    user_order_input = input(
        "\nEnter the index of products you want to add separated by commas.\n")
    create_indexed_list(couriers_list)
    user_courier_input = int(input("\nEnter the index of the courier.\n"))
    # appending to the temp new_customer_order list
    new_customer_orders.append({"Customer_name": customer_name, "Customer_address": customer_address,
                               "Customer_phone_number": customer_phone_number, "Courier": user_courier_input, "Status": "Preparing", "Items": user_order_input})
    return new_customer_orders

# ************display all orders******************


def display_orders(list_file):
    """lists all orders"""
    if len(list_file) == 0:
        pass
    elif len(list_file) < 2:
        print(
            f"There is {len(list_file)} order as shown below:\n")
        for order in list_file:
            print(order)
        print("\n")
    else:
        print(
            f"There are {len(list_file)} orders as shown below:\n")
        for order in list_file:
            print(order)


# ********** changes the order status of an order when passed the order's index*********************


def updates_order_status(order_index, status_index, list_file):
    """ function changes order status of a specific indexed order"""
    if order_index in range(len(list_file)):
        if status_index in range(len(order_status)):
            current_order_status = list_file[order_index]["Status"]
            list_file[order_index]["Status"] = order_status[status_index]
            print(
                f"Order status has been changed from {current_order_status} to {order_status[status_index]}\n")
            print(list_file[order_index])
        else:
            print("Incorrect input or out of range")


def updates_status_csv(all_orders):
    try:
        with open("./orders.csv", "w", newline="", encoding="utf8") as file:
            fieldnames = ["Customer_name", "Customer_address",
                          "Customer_phone_number", "Courier", "Status", "Items"]
            writer = csv.DictWriter(file, fieldnames)
            writer.writeheader()
            for order in all_orders:
                writer.writerow(order)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except IOError:
        print(f"Error: {IOError}")
