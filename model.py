from abc import ABC, abstractmethod
from enum import Enum


class ITrainCommands(ABC):

    @abstractmethod
    def train_pets(self, string):
        ...


class Animals(ABC):

    def __init__(self, name, date_fo_birth):
        self.name = ''
        self.date_fo_birth = ''
        self._list_command = []
        self.type = None

    def command_add(self, command):
        self._list_command.append(command)


class Pets(Animals, ITrainCommands):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)

    def to_string(self):
        return f'Домашнее животное, вид: {self.type}, имя: {self.name}, дата рождения: {self.date_fo_birth}, ' \
               f'подчиняется командам: {self._list_command}'

    def train_pets(self, string):
        self._list_command.append(string)


class PackAnimals(Animals):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)

    def to_string(self):
        return f'Вьючное животное, вид: {self.type}, имя: {self.name}, дата рождения: {self.date_fo_birth}, ' \
               f'подчиняется командам: {self._list_command}'


class Cat(Pets):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)
        self.type = AnimalType.CAT


class Dog(Pets):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)
        self.type = AnimalType.DOG


class Hamster(Pets):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)
        self.type = AnimalType.HAMSTER


class Horse(PackAnimals):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)
        self.type = AnimalType.HORSE


class Camel(PackAnimals):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)
        self.type = AnimalType.CAMEL


class Donkey(PackAnimals):

    def __init__(self, name: str, date_fo_birth: str):
        super().__init__(name, date_fo_birth)
        self.type = AnimalType.DONKEY


class AnimalType(Enum):
    CAT = 'Кот'
    DOG = 'Собака'
    HAMSTER = 'Хомяк'
    HORSE = 'Лошадь'
    CAMEL = 'Верблюд'
    DONKEY = 'Осел'


if __name__ == '__main__':
    pass
