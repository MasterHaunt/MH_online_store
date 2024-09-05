import pytest


def test_category_init(category_1):
    """Тестирование создания объекта класса 'Category', у которого атрибут 'products' содержит список из
    трёх объектов класса 'Product' """
    assert category_1.name == "Category 1"
    assert category_1.description == "First category"
    assert category_1.product_count == 3
    assert category_1.category_count == 1


def test_category_add_product(category_1, product_2):
    """Тестирование метода добавления объекта класса 'Product' в объект класса 'Category' """
    category_1.add_product(product_2)
    assert category_1.product_count == 4


def test_category_add_not_product(category_1):
    """Тестирование выброса ошибки <TypeError> при попытке добавления объекта не из класса 'Product'
     в объект класса 'Category' """
    with pytest.raises(TypeError):
        category_1.add_product("Not product")
    assert category_1.product_count == 3


def test_category_str(category_1):
    """ Тестирование строкового представления объекта класса 'Category' """
    assert str(category_1) == "Category 1, количество продуктов: 410 шт."


def test_iterator(category_iterator):
    """ Тестирование итератора объекта класса 'Category' """
    iter(category_iterator)
    assert category_iterator.index == 0
    assert str(next(category_iterator)) == "Product_1-1, 131.25 руб. Остаток: 100 шт."
    assert str(next(category_iterator)) == "Product_1-2, 187.23 руб. Остаток: 180 шт."
    assert str(next(category_iterator)) == "Product_1-3, 115.96 руб. Остаток: 130 шт."
    with pytest.raises(StopIteration):
        next(category_iterator)
