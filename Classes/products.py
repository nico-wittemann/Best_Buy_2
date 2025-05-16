class Product:
    """
    Represents a product that is stored.
    This class handles methods like activation, deactivation, promotions,
    and buy.

    Attributes:
        active (bool): Indicates if the product is active (default = True).
        promotion (Promotion or None): An optional promotion applied to the product.
     """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance with name, price, and quantity.

        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must not be negative.
            quantity (int): The quantity of the product. Must not be negative.

        Attributes:
            active (bool): Indicates whether the product is active. Defaults to True.
            promotion (None): Indicates if a promotion is applied. Defaults to None.

        Raises:
            ValueError: If name is empty, price is invalid, or quantity is invalid.
        """
        self.name = str(name)
        if self.name == "":
            raise ValueError("Name must not be empty")
        try:
            self.price = float(price)
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number")
        if self.price < 0:
            raise ValueError("Price must be greater than 0")
        self.set_quantity(quantity)
        self.active = True
        self.promotion = None


    def get_promotion(self):
        """
        Calls the promotion set to this product.

        Returns:
            self.promotion or None: The assigned promotion, or None if no promotion is set.
        """
        return self.promotion


    def set_promotion(self, promotion):
        """
        Assigns a promotion to this product.

        Args:
            self.promotion: The promotion to assign.
        """
        self.promotion = promotion


    def get_quantity(self):
        """
        Getter function for quantity.

        Returns:
            self.quantity: The current quantity of the product.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity of product.
        If quantity reaches 0, deactivates the product.

        Args:
            quantity (int): The new quantity. Must not be negative.

        Raises:
            ValueError: If the quantity is invalid or negative.
        """
        try:
            self.quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Invalid quantity provided")
        if self.quantity < 0:
            raise ValueError("Quantity must not be negative")
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """
        Getter function for active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active


    def activate(self):
        """
        Activates the product, making it available for purchase.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product, making it unavailable for purchase.
        """
        self.active = False


    def show(self):
        """
        Presents the product.

        Returns:
             info (str): A string that presents the product, including name, price, quantity. Promotion if active.
        """
        info =  f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            info += f", Promotion: {self.promotion.name}"
        return info

    def buy(self, quantity):
        """
       Process of buying a product.

        Args:
            quantity (int): The quantity to purchase. Must be positive and less than
                            or equal to the available quantity.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is negative or exceeds available stock.
        """
        if quantity > self.quantity:
            raise ValueError("Quantity is too high")
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        self.set_quantity(self.quantity - quantity)
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity



    def __str__(self):
        """
        Returns the product's name.

        Returns:
            str: The name of the product.
        """
        return f"{self.name}"


class NonStockedProduct(Product):
    """
    Represents a product that is always in stock (digital products) it has no quantity.

    Attributes:
        active (bool): Indicates if the product is active (default = True).
        promotion (Promotion or None): An optional promotion applied to the product.
        quantity (int): Always 0 on default
    """

    def __init__(self, name, price):
        """
        Initializes a NonStockedProduct instance.

        Args:
            name (str): The name of the product. Must not be empty.
            price (float): The price of the product. Must not be negative.

        Raises:
            ValueError: If name is empty or price is invalid.
        """
        self.name = str(name)
        if self.name == "":
            raise ValueError("Name must not be empty")
        try:
            self.price = float(price)
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number")
        if self.price < 0:
            raise ValueError("Price must be greater than 0")
        self.active = True
        self.quantity = 0


    def get_quantity(self):
        """
        Always returns False because there is no quantity.

        Returns:
            bool: Always False.
        """
        return False


    def set_quantity(self, quantity):
        """
        Prevents setting quantity for a NonStockedProduct.

        Args:
            quantity (int): The quantity to set (irrelevant for this product type).

        Raises:
            AttributeError: Always raised as quantity is not applicable.
        """
        raise AttributeError("Quantity cannot be set for this product type.")


    def show(self):
        """
        Presents the product. In this case no quantity, cause its digital.

        Returns:
             info (str): A string that presents the product, including name, price. Promotion if active.
        """
        info = f"{self.name}, Price: {self.price}"
        if self.promotion:
            info += f", Promotion: {self.promotion.name}"
        return info


    def buy(self, quantity):
        """
        Processes of buying of a NonStockedProduct.

        Args:
            quantity (int): The quantity to purchase. Must be positive.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is negative.
        """

        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class LimitedProduct(Product):
    """
    Represents a product with a maximum purchase limit per order.

    Attributes:
        maximum (int): The maximum allowed quantity per purchase.
    """
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        try:
            self.maximum = int(maximum)
        except (ValueError, TypeError):
            raise ValueError("Maximum must be a valid number")
        if self.price < 0:
            raise ValueError("Maximum must be greater than 0")


    def show(self):

        """
        Returns a string that presents the product

        Returns:
             info (str): A string that presents the product, including name, price, quantity, maximum. Promotion if active.
        """
        info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"
        if self.promotion:
            info += f", Promotion: {self.promotion.name}"
        return info


    def get_maximum(self):
        """
        Returns the maximum quantity thats allowed in an order.

        Returns:
            int: The maximum quantity allowed per purchase.
        """
        return self.maximum

