## Домашняя работа по уроку 15.1 "Магические методы"
# -----------------------------------------------

Выполнил: Чельтёмов Андрей Владимирович, поток PD 52/0

В данной работе:
- в модуле `product.py` изменено описание класса `Product`:
    * реализован метод `__str__` для строкового представления объекта класса `Product` в виде: `<Название продукта, 80 руб. Остаток: 15 шт.>`;
    * реализован метод `__add__` для сложения двух объектов класса `Product`: складываются результаты умножения цен товаров на их количества;
- в модуле `category.py` изменено описание класса `Category`:
    * реализован метод `__str__` для строкового представления объекта класса `Category` в виде: `<Название категории, количество продуктов: 200 шт.>`;
- в пакете `src` создан модуль `category_iterator.py` - описание класса `CategoryIterator`, использующегося для проведения итераций по товарам заданной категории;
- в пакете `tests` добавлены тесты для нового функционала:
    * в модуле `test_category.py` добавлено тестирование метода строкового отображения объекта класса `Category`; тестирование итератора (объекта класса `CategoryIterator`);
    * в модуле `test_product.py` добавлено тестирование метода строкового отображения объекта класса `Product`; тестирование метода сложения объектов класса `Product`.

Функционал, реализованный ранее: 
- в модуле `category.py` изменено описание класса `Category`:
    * список товаров сделан приватным атрибутом;
    * для добавления товаров в категорию реализован метод `add_product()`;
    * для просмотра списка товаров реализован геттер, возвращающий список товаров в виде строк `<название товара>, <стоимость>, <остаток товара на складе>`;
- в модуле `product.py` изменено описание класса `Product`:
    * цена товара сделана приватным атрибутом;
    * описан геттер для цены товара;
    * описан сеттер для цены товара (при задании цены меньше текущей - запрашивается подтверждение пользователя, при задании нулевой цены - выводится сообщение "Цена не должна быть нулевая или отрицательная" и новая цена не устанавливается)

- в пакете `tests` добавлены тесты для нового функционала:
    * в модуле `test_category.py` добавлено тестирование метода добавления объекта класса `Product` в объект класса `Category`;
    * в модуле `test_product.py` добавлено тестирование метода класса `Product`, создающего объект `Product` из словаря; тестирование сеттера приватного атрибута класса `Product` - цены, при установке цены большей, чем текущая и нулевой цены.

- созданы пакеты: `src`, `tests`;
- в пакете `src` созданы модули:
    * `category.py` - описание класса `Category`;
    * `product.py` - описание класса `Product`;
    * `utils.py` - функция загрузки данных из файла `.json` и создание из загруженных данных объектов классов `Category` и `Product`;
- в пакете `tests` созданы модули:
    * `conftest.py` - фикстуры для тестирования функций;
    * `test_category.py` - тестирование создания объекта класса `Category`;
    * `test_product.py` - тестирование создания объекта класса `Product`;
    * `test_utils.py` - тестирование функции загрузки данных из файла `.json` и создания из загруженных данных объектов классов `Category` и `Product`;
- создан модуль `config.py` для настроек программы, добавлена константа `SOURCE_FILE` - ссылка на файл "products.json";
- создан модуль `data_from_json.py` для проверки функционирования загрузки данных из файла `"SOURCE_FILE"` и создания из загруженных данных объектов классов `Category` и `Product`;
- создан модуль `main.py` в который перенесён код из задания, проверена корректность его работы.