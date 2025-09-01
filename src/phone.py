from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
               Создание экземпляра класса Phone.

               :param name: Название товара(наследуем от родителя).
               :param price: Цена за единицу товара(наследуем от родителя).
               :param quantity: Количество товара в магазине(наследуем от родителя).
               :param number_of_sim: Количество сим-карт.
               """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """
                Магический метод __repr__, возвращает представление класса(для разработчиков)
                """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """
        Геттер для number_of_sim
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        """
                Сеттер для number_of_sim
        """
        if value > 0:
            self._number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
