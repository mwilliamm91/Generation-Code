# **************Courier menu display***********************


def displays_courier_menu():
    """displays courier menu options"""
    print('''------Couriers-------
          0: Return to main menu
          1: View all couriers 
          2: Add a new courier
          3: Update an existing courier
          4: Delete a courier from the list
-----------------------''')

# Adds a new courier and saves to a list and text file


def adds_courier():
    """ adds new couriers into a list and writes the list in a csv file"""
    new_couriers = []
    new_courier = {}
    new_courier_name = input("Enter the new courier's name.\n")
    new_courier_phone = int(input("Enter the courier's phone number. \n"))
    new_courier.update(Name=new_courier_name, Phone_number=new_courier_phone)
    new_couriers.append(new_courier)
    return new_couriers
