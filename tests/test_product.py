import pytest

from src.product import Product


def test_product_init(product_1):
    """ Тестирование создания объекта класса 'Product' """
    assert product_1.name == "Product_1-1"
    assert product_1.description == "Product__1___1"
    assert product_1.price == 131.25
    assert product_1.quantity == 100


def test_new_product():
    """ Тестирование метода класса "Товар", создающего объект 'Product' из словаря """
    product_3 = Product.new_product(
        {
            "name": "Product_3-3",
            "description": "Product__3___3",
            "price": 332.32,
            "quantity": 300,
        }
    )
    assert product_3.name == "Product_3-3"
    assert product_3.description == "Product__3___3"
    assert product_3.price == 332.32
    assert product_3.quantity == 300


def test_product_price_setter(product_1):
    """ Тестирование сеттера приватного атрибута класса 'Product' - цены, при установке цены большей, чем текущая """
    product_1.price = 1000.00
    assert product_1.price == 1000.00


def test_product_null_price_setter(capsys, product_1):
    """ Тестирование сеттера приватного атрибута класса 'Product' - цены, при установке нулевой цены """
    product_1.price = 0.00
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_1.price == 131.25


def test_product_str(product_1):
    """ Тестирование строкового представления объекта класса 'Product' """
    assert str(product_1) == "Product_1-1, 131.25 руб. Остаток: 100 шт."


def test_product_add(product_1, product_2):
    """ Тестирование магического метода сложения объектов класса 'Product' """
    assert product_1 + product_2 == 59569.0


def test_smartphone_init(smartphone_1, smartphone_2):
    """  Тестирование создания объекта класса 'Smartphone'  """
    assert smartphone_1.name == "Smartphone 1"
    assert smartphone_1.description == "Smartphone 1 is a № 1 smartphone"
    assert smartphone_1.price == 10000.0
    assert smartphone_1.quantity == 10
    assert smartphone_1.efficiency == 50.1
    assert smartphone_1.model == "ONE"
    assert smartphone_1.memory == 128
    assert smartphone_1.color == "black"
    assert smartphone_2.name == "Smartphone 2"
    assert smartphone_2.description == "Smartphone 2 is a № 2 smartphone"
    assert smartphone_2.price == 20000.0
    assert smartphone_2.quantity == 20
    assert smartphone_2.efficiency == 50.2
    assert smartphone_2.model == "TWO"
    assert smartphone_2.memory == 256
    assert smartphone_2.color == "white"


def test_lawn_grass_init(lawn_grass_1, lawn_grass_2):
    """  Тестирование создания объекта класса 'LawnGrass'  """
    assert lawn_grass_1.name == "Lawn grass 1"
    assert lawn_grass_1.description == "Lawn grass 1 is a № 1 Lawn grass"
    assert lawn_grass_1.price == 1000.0
    assert lawn_grass_1.quantity == 100
    assert lawn_grass_1.country == "Panama"
    assert lawn_grass_1.germination_period == "3 days"
    assert lawn_grass_1.color == "gray"
    assert lawn_grass_2.name == "Lawn grass 2"
    assert lawn_grass_2.description == "Lawn grass 2 is a № 2 Lawn grass"
    assert lawn_grass_2.price == 2000.0
    assert lawn_grass_2.quantity == 200
    assert lawn_grass_2.country == "Canada"
    assert lawn_grass_2.germination_period == "6 days"
    assert lawn_grass_2.color == "green"


def test_smartphone_plus_grass(smartphone_1, lawn_grass_1):
    """ Тестирование выброса ошибки <TypeError> при попытке суммирования объектов разных классов """
    with pytest.raises(TypeError):
        result = smartphone_1 + lawn_grass_1


def test_smartphone_add(smartphone_1, smartphone_2):
    """ Тестирование суммирования объектов одинакового класса """
    assert smartphone_1 + smartphone_2 == 500000.0


def test_str_smartphone(smartphone_1, smartphone_2):
    """ Тестирование унаследованного от класса 'Product' метода строкового представления в классе 'Smartphone' """
    assert str(smartphone_1) == "Smartphone 1, 10000.0 руб. Остаток: 10 шт."
    assert str(smartphone_2) == "Smartphone 2, 20000.0 руб. Остаток: 20 шт."


def test_str_lawn_grass(lawn_grass_1, lawn_grass_2):
    """ Тестирование унаследованного от класса 'Product' метода строкового представления в классе 'LawnGrass' """
    assert str(lawn_grass_1) == "Lawn grass 1, 1000.0 руб. Остаток: 100 шт."
    assert str(lawn_grass_2) == "Lawn grass 2, 2000.0 руб. Остаток: 200 шт."
