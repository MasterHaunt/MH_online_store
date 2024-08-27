def test_category_init(category_1):
    """Тестирование создания объекта класса 'Category', у которого атрибут 'products' содержит список из
    трёх объектов класса 'Product'"""
    assert category_1.name == "Category 1"
    assert category_1.description == "First category"
    assert category_1.product_count == 3
    assert category_1.category_count == 1


def test_category_add_product(category_1, product_2):
    """Тестирование метода добавления объекта класса "Продукт" в объект класса "Категория" """
    category_1.add_product(product_2)
    assert category_1.product_count == 4
