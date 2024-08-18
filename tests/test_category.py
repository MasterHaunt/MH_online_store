def test_category_init(category_1):
    assert category_1.name == "Category 1"
    assert category_1.description == "First category"
    assert len(category_1.products) == 3
    assert category_1.category_count == 1


def test_product_init(product_1):
    assert product_1.name == "Product_1-1"
    assert product_1.description == "Product__1___1"
    assert product_1.price == 131.25
    assert product_1.quantity == 100
