class Category:
    """Класс категории товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count = len(self.__products)

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        products_list = []
        for i in range(len(self.__products)):
            products_list.append(
                f"{self.__products[i].name}, "
                f"{self.__products[i].price} руб. "
                f"Остаток: {self.__products[i].quantity} шт.")
        return products_list
