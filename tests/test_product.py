from src.product import Product


def test_product_init(product_1):
    """Тестирование создания объекта класса "Товар" """
    assert product_1.name == "Product_1-1"
    assert product_1.description == "Product__1___1"
    assert product_1.price == 131.25
    assert product_1.quantity == 100


def test_new_product():
    """Тестирование метода класса "Товар", создающего объект "Товар" из словаря"""
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
    """Тестирование сеттера приватного атрибута класса "Товар" - цены, при установке цены большей, чем текущая"""
    product_1.price = 1000.00
    assert product_1.price == 1000.00


def test_product_null_price_setter(capsys, product_1):
    """Тестирование сеттера приватного атрибута класса "Товар" - цены, при установке нулевой цены"""
    product_1.price = 0.00
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_1.price == 131.25


def test_product_str(product_1):
    """Тестирование строкового представления объекта класса 'Product'"""
    assert str(product_1) == "Product_1-1, 131.25 руб. Остаток: 100 шт."


def test_product_add(product_1, product_2):
    """Тестирование магического метода сложения объектов класса 'Product'"""
    assert product_1 + product_2 == 59569.0
