import csv
import os


# *****************displays indexed items************************
def create_indexed_list(list_items):
    """ displays indexed list items"""
    for ind, val in enumerate(list_items):
        print(f"{ind}: {val}")


# ********** loops through the key, value pair and changes the value if user requests and saves into a csv file*****************


def updates_key_value(order_index, list_file, link, field_names):
    """ updates key value pairs in a while loop if the user opts to change"""
    if order_index not in range(len(list_file)) and order_index == '':
        print("No property has been changed")
    else:
        print("\n", list_file[order_index], "\n")
        for key in list_file[order_index].keys():
            while True:
                value_input = input(
                    f"Enter the new {key}. Press enter to skip and proceed.\n")
                if value_input == "":
                    print(f"{key} wasn't changed")
                    break
                else:
                    list_file[order_index].update({key: value_input})
                    print(f"The {key} has been changed to {value_input}\n")
                    break

        with open(link, "w", newline="", encoding="utf8") as file:
            headers = field_names
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(list_file)

# *******deletes an order from an indexed list given the index and updates the csv file*********************


def deletes_item(order_index, delete_from_file, link, field_names):
    """ deletes list elements given the index and updates respective csv file"""
    try:
        if order_index in range(len(delete_from_file)):
            delete_from_file.remove(delete_from_file[order_index])
        with open(link, "w", newline="", encoding="utf8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(delete_from_file)
    except FileNotFoundError as fnfe:
        print(f"{fnfe}: error encountered")
    except IndexError:
        print(f"Error: {IndexError}")

# ***********import files (orders, products, couriers) ****************


def load_files(link, container):
    """ imports a list from it's respective csv file"""
    try:
        with open(link, "r", newline="", encoding="utf8") as file:
            contents = csv.DictReader(file)
            for content in contents:
                container.append(content)
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")

# **************adds a new product to a new or existing a csv file********


def save_items(item_list, csv_link, field_names):
    """ function saves new item to a new or existing csv file """
    try:
        if os.path.isfile(csv_link):
            with open(csv_link, "a", newline="", encoding="utf8") as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                for item in item_list:
                    writer.writerow(item)
        else:
            with open(csv_link, "w", newline="", encoding="utf8") as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
                for item in item_list:
                    writer.writerow(item)
    except FileNotFoundError as fnfe:
        print(f"error: {fnfe}")
    except IOError:
        print("I/O error")
