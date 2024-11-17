class Product:

    def __init__(self, name, price, quantity):
        """Get name price and quantity from user and check for valid input with exceptions.
        Set active of new item to default True."""
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
        """Returns the promotion assigned to this product."""
        return self.promotion


    def set_promotion(self, promotion):
        """Assigns a promotion to this product."""
        self.promotion = promotion


    def get_quantity(self):
        """Getter function for quantity.
        Returns the quantity (float)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity with try except
        If quantity reaches 0, deactivates the product."""
        try:
            self.quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Invalid quantity provided")
        if self.quantity < 0:
            raise ValueError("Quantity must not be negative")
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """Getter function for active.
        Returns True if the product is active, otherwise False."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Returns a string that presents the product"""
        info =  f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            info += f", Promotion: {self.promotion.name}"
        return info

    def buy(self, quantity):
        """Get a quantity and check if its to high or negative. Decrease self.quantity by the
        bought amount and return the price of purchase."""
        if quantity > self.quantity:
            raise ValueError("Quantity is too high")
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


    def __str__(self):
        return f"{self.name}"


class NonStockedProduct(Product):

    def __init__(self, name, price): #Note Teacher: I had to call it again, cause we use Products and self.set_quantity(quantity) cant be called here.
            """Get name price and quantity from user and check for valid input with exceptions.
            Set active of new item to default True. Initialize a product with quantity always set to 0."""
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
        """Return False because there is no quantity."""
        return False


    def set_quantity(self, quantity):
        """Raise an exception because quantity is irrelevant."""
        raise AttributeError("Quantity cannot be set for this product type.")


    def show(self):
        """Returns a string that presents the product, in this case no quantity, cause its digital."""
        info = f"{self.name}, Price: {self.price}"
        if self.promotion:
            info += f", Promotion: {self.promotion.name}"
        return info


    def buy(self, quantity):
        """Get a quantity and check if its negative. Return the price of purchase."""
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        """Get name price and quantity from user and check for valid input with exceptions.
        Set active of new item to default True."""
        super().__init__(name, price, quantity)
        try:
            self.maximum = int(maximum)
        except (ValueError, TypeError):
            raise ValueError("Maximum must be a valid number")
        if self.price < 0:
            raise ValueError("Maximum must be greater than 0")


    def show(self):
        """Returns a string that presents the product"""
        info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"
        if self.promotion:
            info += f", Promotion: {self.promotion.name}"
        return info


    def get_maximum(self):
        """Returns the maximum quantity thats allowed in an order."""
        return self.maximum

