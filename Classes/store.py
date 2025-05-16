from .products import Product


class Store():
    """Represents a store that is created, where products are stored form the Product class."""


    def __init__(self, initial_products=None):
        """
        Initializes a Store instance.

        Args:
            initial_products (list): A list of Products to define the List of items in the store.
        """
        self.list_of_products = []
        if initial_products:
            for product in initial_products:
                self.list_of_products.append(product)


    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product: The product to be added.
        """
        self.list_of_products.append(product)


    def remove_product(self, product):
        """
        Removes a product from the store.

        Args:
            product: The product to be removed.

        Raises:
            ValueError: If the product is not in the store.
        """
        self.list_of_products.remove(product)


    def get_total_quantity(self):
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products in the store.
        """
        return sum([item.get_quantity() for item in self.list_of_products])


    def get_all_products(self):
        """
        Returns all products in the store that are active and give back is_active(True).

        Returns:
            list: A list of active Product instances.
        """
        return [product for product in self.list_of_products if product.is_active()]



    def order(self, shopping_list):
        """
        Make an order by reducing product quantities and calculating the total cost.

        Args:
            shopping_list (list): A list of tuples where each tuple contains:
                                  - A Product instance.
                                  - An integer of the quantity to purchase.

        Returns:
            float: The total price of the order.

        Raises:
            TypeError: If "shopping_list" is not a list or if the elements of "shopping_list" are not tuples
                       with a Product instance and an integer.
            ValueError: If the tuple in "shopping_list" does not have exactly two elements.
        """
        order_price = 0.0
        if not isinstance(shopping_list, list):
            raise TypeError("shopping_list has to be a list")
        for item_order in shopping_list:
            if not isinstance(item_order, tuple) and len(tuple) != 2:
                raise ValueError("Order has to be a Tuple with 2 elements.")
            if not isinstance(item_order[0], Product) and not isinstance(item_order[1], int):
                raise TypeError("First element has to be a product and second a integer.")
            order_price += item_order[0].buy(item_order[1])
        return order_price


