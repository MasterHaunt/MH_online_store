class MixinStr:
    """Класс-миксин для вывода в консоль сведений о создаваемом объекте"""

    def __init__(self):
        """Метод-конструктор выводит на печать строку заданного шаблона, созданную методом __repr__"""
        print(repr(self))

    def __repr__(self):
        """Магический метод для строкового отображения сведений о создаваемом объекте"""
        return f" > {self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"
