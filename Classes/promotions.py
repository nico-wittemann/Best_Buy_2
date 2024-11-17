from abc import ABC, abstractmethod


class Promotion:

    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Abstract method for Promotion calculation"""
        pass


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        """Calculates price with discount."""
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        """Calculate price for Second item half price."""
        pairs = quantity // 2
        reminder = quantity % 2
        return (pairs * 1.5 + reminder) *  product.price



class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        """Calculate price for every third item is free"""
        group_of_three = quantity // 3
        reminder = quantity % 3
        return (group_of_three * 2 + reminder) * product.price