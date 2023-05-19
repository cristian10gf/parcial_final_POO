from abc import ABC
from src.core.planet import Planet

def generar_siguiente_hexadecimal():
    if 'ultimo_hex' not in generar_siguiente_hexadecimal.__dict__:
        generar_siguiente_hexadecimal.ultimo_hex = 1
    
    # Incrementar el último número generado
    generar_siguiente_hexadecimal.ultimo_hex += 1
    
    # Convertir el número a hexadecimal de 6 dígitos
    siguiente_hex = hex(generar_siguiente_hexadecimal.ultimo_hex)[2:].zfill(6)
    
    return siguiente_hex


class Person(ABC):
    id_stringhex = '000000'

    def __init__(self, name: str, planet: 'Planet') -> None:
        self._id_string = Person.id_stringhex
        self._name = name
        self._planet = planet
        Person.id_stringhex = generar_siguiente_hexadecimal()


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
