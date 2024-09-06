from src.product import Product


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

    def __str__(self):
        """Магический метод строкового отображения для объекта класса 'Category'"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """Метод добавления объекта класса "Товар" в приватный атрибут класса "Категория" - список товаров.
        При попытке добавить товар, не являющийся объектом класса или подкласса 'Product' инициализируется
         исключение <TypeError>"""
        if not isinstance(product, Product):
            raise TypeError("Невозможно добавить товар в данный класс")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Метод вывода данных, содержащихся в приватном атрибуте объекта класса "Категория" - списке товаров"""
        products_list = []
        for i in range(len(self.__products)):
            products_list.append(
                f"{self.__products[i].name}, "
                f"{self.__products[i].price} руб. "
                f"Остаток: {self.__products[i].quantity} шт."
            )
        return products_list
