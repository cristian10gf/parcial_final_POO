from abc import ABC
from src.core.planet import Planet

def generar_hexadecimal_secuencial():
    secuencia = 0
    while True:
        hex_secuencial = format(secuencia, '06X')
        yield hex_secuencial
        secuencia += 1


class Person(ABC):
    id_stringhex = generar_hexadecimal_secuencial()

    def __init__(self, name: str, planet: 'Planet') -> None:
        self._id_string = Person.id_stringhex
        self._name = name
        self._planet = planet
        Person.id_stringhex = generar_hexadecimal_secuencial()

    @property
    def id_string(self) -> str:
        return self._id_string

    @property
    def name(self) -> str:
        return self._name

    @property
    def planet(self) -> 'Planet':
        return self._planet




class Soldier(Person):
    def __init__(self, name: str,age: int, planet: 'Planet') -> None:
        super().__init__(name, planet)
        self.__age = age


class Bureaucrat(Person):
    def __init__(self, name: str, planet: 'Planet', department: str) -> None:
        super().__init__(name, planet)
        self.__department = department
