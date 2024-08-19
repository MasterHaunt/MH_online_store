import json
import os.path

from src.category import Category
from src.product import Product


def create_data_from_json(filename: str) -> list:
    """Функция загрузки данных из файла `.json` и создания из загруженных данных объектов классов
    `Category` и `Product`"""
    full_filename = os.path.abspath(filename)
    with open(full_filename, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
    categories = []
    for category in json_data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
