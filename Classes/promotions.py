from abc import abstractmethod


class Promotion:
    """
    Base class for product promotions. This one is not to be used, but the child classes are.
    """

    def __init__(self, name):
        """
        Initializes the Promotion instance.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Abstract method for Promotion calculation.
        """
        pass


class PercentDiscount(Promotion):
    """
    Promotion applies a percentage discount to the total price.
    """

    def __init__(self, name, percent):
        """
        Initializes the PercentDiscount instance.

        Args:
            name (str): The name of the promotion.
            percent (float): The percentage discount to apply (0-100).
        """
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        """
        Calculates the total price after applying the percentage discount.

        Args:
            product: Object name to target its price.
            quantity (int): The quantity purchsed.

        Returns:
            float: The total price after applying the percentage discount.
        """
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """
    A promotion where every second item is sold at half price.
    """

    def apply_promotion(self, product, quantity):
        """
        Calculate total price for Second item half price.

        Args:
            product: Object name to target its price.
            quantity (int): The quantity purchsed.

        Returns:
            float: The total price after applying the second-half price promotion.
        """
        pairs = quantity // 2
        reminder = quantity % 2
        return (pairs * 1.5 + reminder) *  product.price



class ThirdOneFree(Promotion):
    """
    A promotion where every third item is free.
    """

    def apply_promotion(self, product, quantity):
        """
        Calculate total price for every third item is free.

        Args:
            product: Object name to target its price.
            quantity (int): The quantity purchased.

        Returns:
            float: The total price after applying the third-one-free promotion.
        """
        group_of_three = quantity // 3
        reminder = quantity % 3
        return (group_of_three * 2 + reminder) * product.price