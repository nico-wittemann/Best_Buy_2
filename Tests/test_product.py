import pytest
from bestbuy.Classes import Product


def test_create_product():
    bose = Product("Bose", 500, 200)
    assert isinstance(bose, Product)


def test_empty_name():
    with pytest.raises(ValueError, match="Name must not be empty"):
        Product("", 500, 200)


def test_negative_price():
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        Product("Bose", -500, 200)


def test_product_0_quantity_then_inactive():
    bose = Product("Bose", 500, 200)
    bose.set_quantity(0)
    assert not bose.is_active()


def test_product_purchase_modifies_quantity_and_returns_right_output():
    bose = Product("Bose", 500, 200)
    assert bose.buy(10) == 5000
    assert bose.get_quantity() == 190


def test_bought_quantity_too_big():
    bose = Product("Bose", 500, 200)
    with pytest.raises(ValueError, match="Quantity is too high"):
        bose.buy(300)
