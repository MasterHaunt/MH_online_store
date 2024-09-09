from src.product import Product, Smartphone, LawnGrass


def test_mixin_str(capsys):
    """Тестирование класса-миксина, выводящего информацию о создаваемом объекте"""
    Product("Product_M-1", "Product__M___1", 222.33, 50)
    message = capsys.readouterr()
    assert message.out.strip() == "> Product (Product_M-1, Product__M___1, 222.33, 50)"

    Smartphone(
        "Smartphone 1",
        "Smartphone 1 is a № 1 smartphone",
        10000.0,
        10,
        50.1,
        "ONE",
        128,
        "black",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "> Smartphone (Smartphone 1, Smartphone 1 is a № 1 smartphone, 10000.0, 10)"
    )

    LawnGrass(
        "Lawn grass 1",
        "Lawn grass 1 is a № 1 Lawn grass",
        1000.0,
        100,
        "Panama",
        "3 days",
        "gray",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "> LawnGrass (Lawn grass 1, Lawn grass 1 is a № 1 Lawn grass, 1000.0, 100)"
    )
