class Product:
    """Класс товара"""

    name: str
    description: str
    price: float
    quantity: int
    products_list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_list.append(
            {
                "name": name,
                "description": description,
                "price": price,
                "quantity": quantity,
            }
        )

    def __str__(self):
        """Магический метод строкового отображения для объекта класса 'Product'"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод сложения для объекта класса 'Product':
         складывается произведение количества товара на его стоимость"""
        return (self.quantity * self.price) + (other.quantity * other.price)

    @classmethod
    def new_product(cls, product_properties: dict):
        """Метод создания объекта класса "Товар" из словаря"""
        for product in cls.products_list:
            if product["name"] == product_properties["name"]:
                product_properties["quantity"] += product["quantity"]
                if product["price"] < product_properties["price"]:
                    product["price"] = product_properties["price"]
                else:
                    product_properties["price"] = product["price"]

        return cls(
            product_properties["name"],
            product_properties["description"],
            product_properties["price"],
            product_properties["quantity"],
        )
        # По доп. условию, если добавляется товар, имеющийся в категории, программа устанавливает ту цену, которая
        # больше, а количества имеющегося и добавляемого товара суммируется. При этом, полагаю, имеющийся товар
        # необходимо из категории удалять, но способ это сделать я "с наскока" не нашёл.

    @property
    def price(self):
        """Геттер для получения значения приватного атрибута - цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для задания значения приватного атрибута - цены"""
        if new_price <= 0.0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            if input("Введите символ 'y' для подтверждения меньшей цены: ") == "y":
                self.__price = new_price
        else:
            self.__price = new_price
        return self.__price
