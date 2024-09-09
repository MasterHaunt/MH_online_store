from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс продукта"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
