# ****************Product menu display*******************
def displays_product_menu():
    """ functions displays all product menu options"""
    print("""-----PRODUCTS-----
    0. Return to main menu
    1. View all products
    2. Add a new Product
    3. Update Product
    4. Delete Product
---------------------""")

# **********takes user input for new product***********


def add_product():
    """takes user product input and appends it to a list """
    new_product_list = []
    new_product = {}
    product_name = input("\nEnter the name of the product to add \n")
    product_price = float(input("\nEnter the all_products's price \n"))
    new_product.update(Name=product_name, Price=product_price)
    new_product_list.append(new_product)
    print(f"added {product_name} to the product list.")
    return new_product_list
