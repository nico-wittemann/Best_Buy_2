from Classes.store import Store
from Classes.products import Product


def start(store, product_list):
    """Prints the user_interface in a loop. Handles the user input and sends
    him to the required function, while handling errors."""
    while True:
        store_functions ={1: list_all_products_in_store,
                          2: show_total_amount_in_store,
                          3: make_an_order,}
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        try:
            user_choice = int(input("Please choose a number: "))
            if not (1 <= user_choice <= 4):
                raise ValueError()
            if user_choice == 4:
                print("Have a nice day!")
                break
            elif user_choice == 3:
                store_functions[user_choice](store, product_list)
            else:
                store_functions[user_choice](store)
        except ValueError:
            print("Enter a number between 1 and 4.")
        print()


def list_all_products_in_store(store):
    """Lists every product in the store. Numbered by the index of the list + 1."""
    list_of_products = store.get_all_products()
    print("------")
    for i, product in enumerate(list_of_products, 1):
        print(f"{i}. {product}")
    print("------")


def show_total_amount_in_store(store):
    """Prints the total amount of items available at the store."""
    print(f"Total of {store.get_total_quantity()} in store.")


def make_an_order(store, product_list):
    """Gets store Class and the list of products. Creates a List of the orders by prompting
    another function to give back a order_tuple as long as the user wants to add items.
    Then gets the order from the store and print the price."""
    order_list = []
    list_all_products_in_store(store)
    print("When you want to finish order, enter empty text.")
    while True:
        order_tuple = get_item_and_quantity(product_list)
        if order_tuple == "break":
            break
        elif isinstance(order_tuple, tuple) and len(order_tuple) == 2:
            order_list.append(order_tuple)
            print("Product added to list!")
    order_price = store.order(order_list)
    print(f"Order made! Total payment: ${order_price}")


def get_item_and_quantity(product_list):
    """First get the product number then the quantity of the order with error management.
     Then return a tuple of the order."""
    # Get product number
    product_number = input("Which product number do you want?")
    if product_number == "":
        return "break"
    try:
        product_number = int(product_number)
        if product_number > len(product_list):
            print("Invalid input. Pick a number from the list.")
            return
        index = product_number - 1
        ordered_product = product_list[index]
    except ValueError:
        print("Invalid input.")
        return
    # Get quantity
    quantity = input("Which amount do you want?")
    if quantity == "":
        return "break"
    try:
        quantity = int(quantity)
    except ValueError:
        print("Invalid input.")
        return
    return (ordered_product, quantity)


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    store = Store(product_list)
    start(store, product_list)


if __name__ == "__main__":
    main()


#Komments für functions
#Ordner sortieren!