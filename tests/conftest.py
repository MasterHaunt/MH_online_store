import pytest

from src.category import Category
from src.product import Product
from src.cetegory_iterator import CategoryIterator


@pytest.fixture
def category_1():
    return Category(
        name="Category 1",
        description="First category",
        products=[
            Product("Product_1-1", "Product__1___1", 131.25, 100),
            Product("Product_1-2", "Product__1___2", 187.23, 180),
            Product("Product_1-3", "Product__1___3", 115.96, 130),
        ],
    )


@pytest.fixture
def product_1():
    return Product("Product_1-1", "Product__1___1", 131.25, 100)


@pytest.fixture
def product_2():
    return Product("Product_2-2", "Product__2___2", 232.22, 200)


@pytest.fixture
def category_iterator(category_1):
    return CategoryIterator(category_1)
