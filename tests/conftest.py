import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass
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


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Smartphone 1",
        "Smartphone 1 is a № 1 smartphone",
        10000.0,
        10,
        50.1,
        "ONE",
        128,
        "black",
    )


@pytest.fixture
def smartphone_2():
    return Smartphone(
        "Smartphone 2",
        "Smartphone 2 is a № 2 smartphone",
        20000.0,
        20,
        50.2,
        "TWO",
        256,
        "white",
    )


@pytest.fixture
def lawn_grass_1():
    return LawnGrass(
        "Lawn grass 1",
        "Lawn grass 1 is a № 1 Lawn grass",
        1000.0,
        100,
        "Panama",
        "3 days",
        "gray",
    )


@pytest.fixture
def lawn_grass_2():
    return LawnGrass(
        "Lawn grass 2",
        "Lawn grass 2 is a № 2 Lawn grass",
        2000.0,
        200,
        "Canada",
        "6 days",
        "green",
    )
