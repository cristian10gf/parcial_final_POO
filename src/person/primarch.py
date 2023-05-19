from src.person.person import Person
from src.enumeration.enumeration import Status

class Primarch(Person):
    def __init__(self, name: str, planet: 'Planet', alias: str, status: 'Status', imperium: 'Imperium') -> None:
        super().__init__(name, planet)
        self.__alias = alias
        self.__loyalty = True

        self.__status = status
        self.__imperium = imperium
        print(f'The Emperor created Primarch {self.name}')

    def change_status(self, status: Status) -> None:
        self.__status = status

    def betray(self) -> None:
        self.__loyalty = False
        print(f'Primarch {self.name} betrays the Emperor')

    @property
    def alias(self) -> str:
        return self.__alias
    
    @property
    def status(self) -> 'Status':
        return self.__status
    
    @property
    def loyalty(self) -> bool:
        return self.__loyalty

