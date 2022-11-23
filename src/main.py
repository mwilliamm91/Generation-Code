from utils import updates_key_value, deletes_item, load_files, save_items, create_indexed_list
from file_handlers.orders import creates_order, displays_order_menu, display_orders, order_status, updates_order_status, updates_status_csv
from file_handlers.products import displays_product_menu, add_product
from file_handlers.couriers import displays_courier_menu, adds_courier


def displays_main_menu():
    """ display main menu options"""
    print("\nWelcome to the app\n")
    print('''
        0. Quit the app
        1. Show product menu
        2. Show the courier menu
        3. Show order menu \n 
          ''')


# ******loading all files*************
all_orders = []
load_files("../data/orders.csv", all_orders)
all_products = []
load_files("../data/products.csv", all_products)
all_couriers = []
load_files("../data/couriers.csv", all_couriers)

while True:
    displays_main_menu()
    #  GET user input for main menu option
    start_app_input = int(input("Select input as shown above \n"))

    if start_app_input == 0:
        # quits app if the user select 0
        print("quitting the app")
        break
    elif start_app_input == 1:
        # input selections for the product menu
        while True:
            displays_product_menu()
            product_menu_input = int(input("Select input as shown above \n"))
            if product_menu_input == 0:
                print("...returning to main menu")
                break
            elif product_menu_input == 1:
                print(
                    f"\n There are {len(all_products)} products as shown below:\n")
                for prod in all_products:
                    print(prod)
                continue
            elif product_menu_input == 2:
                added_product = add_product()
                save_items(added_product, "../data/products.csv",
                           ["Name", "Price"])
                continue
            elif product_menu_input == 3:
                create_indexed_list(all_products)
                item_to_update = int(
                    input("\nEnter index of product to update\n"))
                updates_key_value(item_to_update, all_products,
                                  "../data/products.csv", ["Name", "Price"])
                continue
            elif product_menu_input == 4:
                print("\n")
                create_indexed_list(all_products)
                item_to_delete = int(
                    input("\nEnter index of item to delete \n"))
                deletes_item(item_to_delete, all_products,
                             "../data/products.csv", ["Name", "Price"])
                print("Product has been deleted")
                continue
            else:
                print("Invalid input. Please try again.\n")
                continue

    elif start_app_input == 2:
        while True:
            displays_courier_menu()

            courier_menu_options = int(
                input("Select an input as shown above \n"))
            # input selections for the courier menu
            if courier_menu_options == 0:
                print("....returning to main menu \n")
                break
            elif courier_menu_options == 1:
                print(
                    f"There are {len(all_couriers)} couriers as shown below:\n")
                for courier in all_couriers:
                    print(courier)
                continue
            elif courier_menu_options == 2:
                added_courier = adds_courier()
                print(added_courier)
                save_items(added_courier, "../data/couriers.csv",
                           ["Name", "Phone_number"])
                continue
            elif courier_menu_options == 3:
                create_indexed_list(all_couriers)
                courier_index_input = int(
                    input("\n Enter the index to update an existing courier \n"))
                updates_key_value(courier_index_input, all_couriers,
                                  "../data/couriers.csv", ["Name", "Phone_number"])
                continue
            elif courier_menu_options == 4:
                create_indexed_list(all_couriers)
                courier_index_input = int(
                    input("\n Enter the index to delete an existing courier \n"))
                deletes_item(courier_index_input, all_couriers,
                             "../data/couriers.csv", ["Name", "Phone_number"])
                print("Courier has been deleted")
                continue
            else:
                print("Enter a valid input!")

    elif start_app_input == 3:
        while True:
            displays_order_menu()

            order_menu_options = int(input("Select input as shown above \n"))
            # input selections for the order menu

            if order_menu_options == 0:
                print("....returning to main menu \n")
                break
            elif order_menu_options == 1:
                display_orders(all_orders)
                continue
            elif order_menu_options == 2:
                new_orders = creates_order(all_products, all_couriers)
                save_items(new_orders, "../data/orders.csv", ["Customer_name", "Customer_address",
                                                              "Customer_phone_number", "Courier", "Status", "Items"])
                continue
            elif order_menu_options == 3:
                create_indexed_list(all_orders)
                order_index_input = int(
                    input("Enter the order index to proceed \n"))
                create_indexed_list(order_status)
                order_status_input = int(
                    input("Enter the chosen order status index as displayed above \n"))
                updates_order_status(
                    order_index_input, order_status_input, all_orders)
                #  updating order status in the csv file
                updates_status_csv(all_orders)
                continue
            elif order_menu_options == 4:
                create_indexed_list(all_orders)
                selected_input = int(input("\nEnter the index to update \n"))
                updates_key_value(selected_input, all_orders, "../data/orders.csv", ["Customer_name",
                                                                                     "Customer_address", "Customer_phone_number", "Courier", "Status", "Items"])
                continue
            elif order_menu_options == 5:
                create_indexed_list(all_orders)
                selected_input = int(input("\nEnter the index to delete\n"))
                deletes_item(selected_input, all_orders, "../data/orders.csv", ["Customer_name",
                                                                                "Customer_address", "Customer_phone_number", "Courier", "Status", "Items"])
                continue
            else:
                print("Enter a valid input")

    else:
        print("Invalid input. Please try again")
