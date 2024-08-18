from config import SOURCE_FILE
from src import utils

if __name__ == "__main__":
    categories = utils.create_data_from_json(SOURCE_FILE)
    print(categories[0].name)
    print(categories[0].description)
    print(categories[0].products[0].name)
    print(categories[1].name)
    print(categories[1].description)
    print(categories[1].products[0].name)
