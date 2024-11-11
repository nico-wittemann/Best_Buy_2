class Product:
    active = True


    def __init__(self, name, price, quantity):
        """Get name price and quantity from user and check for valid input with exceptions.
        Set active of new item to default True."""
        self.name = str(name)
        if self.name == "":
            raise ValueError("Name must not be empty")
        try:
            self.price = float(price)
            if self.price < 0:
                raise ValueError("Price must be greater than 0")
        except (ValueError, TypeError):
            print("Invalid price provided.")
        self.set_quantity(quantity)
        self.active = Product.active


    def get_quantity(self):
        """Getter function for quantity.
        Returns the quantity (float)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity with try except
        If quantity reaches 0, deactivates the product."""
        try:
            self.quantity = int(quantity)
            if self.quantity < 0:
                raise ValueError("Quantity must not be negative")
        except (ValueError, TypeError):
            print("Invalid quantity provided")
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
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """Get a quantity and check if its to high or negative. Decrease self.quantity by the
        bought amount and return the price of purchase."""
        if quantity > self.quantity:
            raise ValueError("Quantity is too high")
        if quantity < 0:
            raise ValueError("Quantity must not be negative")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity


#Testing
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

bose.set_quantity(1000)
print(bose.show())

