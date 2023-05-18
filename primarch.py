from src.person.person import Person
from src.enumeration.enumeration import Status

class Primarch(Person):
    def __init__(self, name: str, planet: 'Planet', alias: str, status: 'Status', imperium: 'Imperium') -> None:
        super().__init__(name, planet)
        self.__alias = alias
        self.__loyalty = True

        self.__status = status
        self.__imperium = imperium
        self.__imperium.add_primarch(self)

    def change_status(self, status: Status) -> None:
        self.__status = status

    def betray(self) -> None:
        self.__loyalty = False
        print(f'Primarch {self.name} betrays the Emperor')

