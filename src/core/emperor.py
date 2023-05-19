from src.core.imperium import Imperium
from src.core.planet import Planet
from src.enumeration.enumeration import Status
from src.person.primarch import Primarch
from src.person.person import Person
from src.divisiones.divisions import Segmentum
from src.person.astarte import Astarte


class SingletonError(Exception):
    print('There can only be one Emperor of Mankind')


class Singleton:
   

    def _init_(self) -> None:
        
        # Attributes
        print('The Emperor of Mankind has arisen')
        
        

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE is None:
            raise SingletonError(f'There is no {cls.__name__} instance')
        return cls.__INSTANCE




class Emperor:
    __INSTANCE = None

    def __init__(self) -> None:
        if not Emperor.__INSTANCE is None:
            raise SingletonError('There can be only one Emperor of Mankind')
        else:
            self.__imperium = None
            print('The Emperor of Mankind has arisen')
            Emperor.__INSTANCE = self

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE is None:
            raise SingletonError(f'There is no {cls.__name__} instance')
        return cls.__INSTANCE

    def create_imperium(self, name: str, planet_info: dict) -> None:
        planeta = Planet(planet_info['planet_name'], planet_info['planet_type'])
        segmento = Segmentum(planet_info['segmentum_name'], planet_info['segmentum_location'], [planeta])
        self.__imperium = Imperium(name, planeta, [segmento], self)

    def get_imperium(self) -> 'Imperium':
        return self.__imperium
    
    def set_imperium(self, imperium: 'Imperium'):
        self.imperium = imperium

    def create_primarch(self, name: str = None, alias: str = None, planet_info: dict = None) -> None:
        if name != None:
            primarca_datos = [name, alias, planet_info]
        else:
            primarca_datos = []
        self.__imperium.add_primarch(primarca_datos)
