## Домашняя работа по уроку 17.1 "Исключения"
# -----------------------------------------------

Выполнил: Чельтёмов Андрей Владимирович, поток PD 52/0

В данной работе:
- в модуле `product.py` дополнено описание класса `Product`: при вызове метода `__init__` проверяется, что цена товара не нулевая и не отрицательная, в противном случае - выбрасывается исключение;
- в модуле `category.py` дополнено описание класса `Category`: добавлен метод `middle_price`, рассчитывающий и возвращающий среднюю цену товаров в категории. Если в категории товаров нет - происходит обработка исключения деления на ноль, с выводом сообщения `В категории нет товаров, средняя цена = 0 `, в таком случае метод возвращает "0";
- в пакете `tests` добавлены тесты для нового функционала:
    * В модуле `conftest.py` добавлена фикстура `category_empty` - категория, в которой список товаров пуст;
    * в модуле `test_category.py` добавлено тестирование метода расчёта средней цены товаров в категории, а также тестирование метода расчёта средней цены товаров в пустой категории;
    * в модуле `test_product.py` добавлено тестирование создания объекта класса `Product` с нулевым количеством.


Функционал, реализованный ранее:
- в пакете `src` созданы модули:
    * `base_product.py` - описание абстрактного класса `BaseProduct`;
    * `mixin_str.py` - описание класса-миксина `MixinStr`, выводящего в консоль при инициализации информацию о создаваемом объекте в виде строки: `' > {Имя класса} ( {Наименование товара}, {Описание товара}, {Цена товара}, {Остаток товара на складе}`;
- в модуле `product.py` дополнено описание класса `Product`: классами-родителями указаны `BaseProduct` и `MixinStr`; в метод `__init__` добавлен вызов метода `__init__` класса-миксина `MixinStr`, который, в свою очередь, при инициализации выводит в консоль сведения о создаваемом объекте;
- в пакете `tests` создан модуль `test_mixin_str.py`, в котором реализован тест для нового функционала:
    * тестирование работы методов класса-миксина `MixinStr` при создании объектов классов `Product`, `Smartphone` и `LawnGrass`. 

- в модуле `product.py` добавлены описания двух классов, наследующих от класса `Product`: 
* «Смартфон» (`Smartphone`), к которому добавлены свойства: производительность (`efficiency`), модель (`model`), объем встроенной памяти (`memory`), цвет (`color`);
* «Трава газонная» (`LawnGrass`)к которому добавлены свойства: страна-производитель (`country`), срок прорастания (`germination_period`), цвет (`color`).
- в модуле `product.py` дополнено описание метода `__add__` класса `Product`: включена проверка совпадения складываемых объектов.
- в модуле `category.py` дополнено описание метода `add_product()`: включена проверка типа добавляемого объекта. Если добавляемый объект не принадлежит к классу `Product` или его подклассу - выбрасывается исключение.
- в пакете `tests` добавлены тесты для нового функционала:
    * в модуле `test_category.py` добавлено тестирование метода добавления строкового объекта в перечень товаров объекта класса `Category` (проверяется выброс исключения);
    * в модуле `test_product.py` добавлено тестирование методов создания и строкового отображения объектов классов `Smartphone` и `LawnGrass`; тестирование унаследованного метода сложения объектов класса `Smartphone`, тестирование метода сложения объектов класса `Smartphone` и `LawnGrass` (проверяется выброс исключения).

 - в модуле `product.py` изменено описание класса `Product`:
    * реализован метод `__str__` для строкового представления объекта класса `Product` в виде: `<Название продукта, 80 руб. Остаток: 15 шт.>`;
    * реализован метод `__add__` для сложения двух объектов класса `Product`: складываются результаты умножения цен товаров на их количества;
- в модуле `category.py` изменено описание класса `Category`:
    * реализован метод `__str__` для строкового представления объекта класса `Category` в виде: `<Название категории, количество продуктов: 200 шт.>`;
- в пакете `src` создан модуль `category_iterator.py` - описание класса `CategoryIterator`, использующегося для проведения итераций по товарам заданной категории;
- в пакете `tests` добавлены тесты для нового функционала:
    * в модуле `test_category.py` добавлено тестирование метода строкового отображения объекта класса `Category`; тестирование итератора (объекта класса `CategoryIterator`);
    * в модуле `test_product.py` добавлено тестирование метода строкового отображения объекта класса `Product`; тестирование метода сложения объектов класса `Product`.

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