def test_product_init(product_1):
    """Тестирование создания объекта класса 'Product'"""
    assert product_1.name == "Product_1-1"
    assert product_1.description == "Product__1___1"
    assert product_1.price == 131.25
    assert product_1.quantity == 100
