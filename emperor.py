from src.core.imperium import Imperium
from src.core.planet import Planet
from src.enumeration.enumeration import Status
from src.person.primarch import Primarch
from src.person.person import Person
from src.divisiones.divisions import Segmentum


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
            raise SingletonError('There can be only one instance')
        else:
            self.__imperium = None
            print('The Emperor of Mankind has arisen')
            Emperor.__INSTANCE = self

    def create_imperium(self, name: str, planet_info: dict) -> None:
        planeta = Planet(planet_info['planet_name'], planet_info['planet_type'])
        segmento = Segmentum(planet_info['segmentum_name'], planet_info['segmentum_location'], [planeta])
        Imperium(name, planeta, [segmento], self)


    def create_primarch(self, name: str = None, alias: str = None, planet_info: dict = None) -> None:
        primarca_datos = [name, alias, planet_info]
        if name is None:
            self.__imperium.add_primarch(None)
        else:
            self.__imperium.add_primarch(primarca_datos)
