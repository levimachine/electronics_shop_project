import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self) -> str:
        """
        name getter
        :return: Возвращает имя
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        name setter, проверяет на длину слова. Если больше 10 - обрезает до первых 10 символов.
        :param new_name: Новое имя
        """
        if len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """
        Класс метод, открывает файл items.csv с помощью контекстного менеджера, и создает экземпляры класса в атрибут класса all.
        :param file_path: Путь до файла.
        """
        with open(file=file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for element in reader:
                Item.all.append(
                    cls(name=element['name'], price=float(element['price']), quantity=int(element['quantity'])))

    @staticmethod
    def string_to_number(user_string: str) -> int:
        """
        Статичный метод, делает из строки число, округляет до целого числа "в пол".
        :param user_string: Строка пользователя.
        :return: Число.
        """
        return int(float(user_string))
