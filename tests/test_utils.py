from config import SOURCE_FILE
from src import utils


def test_create_data_from_json():
    """Тестирование функции загрузки данных из файла `.json` и создания из загруженных данных объектов классов
    `Category` и `Product`"""
    assert utils.create_data_from_json(SOURCE_FILE)[0].name == "Смартфоны"
    assert utils.create_data_from_json(SOURCE_FILE)[0].description == (
        "Смартфоны, как средство не только коммуникации,"
        " но и получение дополнительных функций для удобства жизни"
    )
    assert (
        utils.create_data_from_json(SOURCE_FILE)[0].products[0].name
        == "Samsung Galaxy C23 Ultra"
    )
    assert (
        utils.create_data_from_json(SOURCE_FILE)[0].products[0].description
        == "256GB, Серый цвет, 200MP камера"
    )
    assert utils.create_data_from_json(SOURCE_FILE)[0].products[0].price == 180000.0
    assert utils.create_data_from_json(SOURCE_FILE)[0].products[0].quantity == 5
