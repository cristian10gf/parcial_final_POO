from src.person.primarch import Primarch
from src.person.person import Person, Planet
from src.divisiones.divisions import AdeptusAstartes
#from src.core.emperor import  SingletonError
from src.divisiones.divisions import Segmentum, AstraMilitarum
from src.divisiones.divisions import Administratum, Regiment, Chapter
from src.enumeration.enumeration import Status, PlanetType


class RuntimeError(Exception):
    pass


class Imperium:
    __INSTANCE = None

    def __init__(self, name: str, planet: Planet, segmentums: list['Segmentum'], emperor: 'Emperor') -> None:
        self.__name = name
        self.__planet = planet
        if len(segmentums) > 5 and len(segmentums) < 1:
            raise RuntimeError('There can only be 5 Segmentums')
        else:
            self.__segmentums = segmentums
        self.__emperor = emperor
        Imperium.__INSTANCE = self
        self.__primarchs: list['Primarch'] = []
        self.__administratum = Administratum()
        self.__adeptus_astarte = AdeptusAstartes()
        self.__astra_militarum: 'AstraMilitarum' = AstraMilitarum()
        print(f'The Emperor created {self.__name} at planet {self.planet.nombre}')
        print(f'Added Segmentum {self.__segmentums[0].name} to the Imperium')

    @property
    def segmentums(self) -> list['Segmentum']:
        return self.__segmentums

    def crear_planeta(self, info: dict) -> 'Planet':
        planetas = []
        for segmento in self.__segmentums:
            planetas.extend(segmento.planets)
        for planeta in planetas:
            if planeta.nombre == info['planet_name']:
                return planeta
        new_planeta = Planet(info['planet_name'], info['planet_type'])
        return new_planeta

    def crear_segmentum(self, info: dict) -> 'Segmentum':
        for segmento in self.__segmentums:
            if segmento.name == info['segmentum_name']:
                return segmento
        new_segmentum = Segmentum(info['segmentum_name'], info['segmentum_location'], [])
        self.add_segmentum(new_segmentum)
        return new_segmentum
        

    def add_chapter(self, name: str, primarch: 'Primarch', planet: str):
        info_planet = {
            'planet_name': planet,
            'planet_type': 'planet'
        }
        planeta = self.crear_planeta(info_planet)
        chapter = Chapter(name, primarch, planeta)
        self.__adeptus_astarte.add_chapter(chapter)

    def get_chapter(self, index: int) -> 'Chapter':
        return self.__adeptus_astarte.get_chapter(index)
    
    @property
    def planet(self) -> 'Planet':
        return self.__planet

    @property
    def emperor(self) -> 'Emperor':
        return self.__emperor

    @property
    def name(self) -> str:
        return self.__name

    def add_segmentum(self, segmentum: 'Segmentum') -> None:
        self.__segmentums.append(segmentum)
        print(f'Added Segmentum {segmentum.name} to the Imperium')

    def add_primarch(self, primarch_dates: list) -> None:
        if len(primarch_dates) == 0:
            self.__primarchs.append(None)
            print(f'The Emperor created Primarch *****')
        else:
            segmento = self.crear_segmentum(primarch_dates[2])
            planeta = self.crear_planeta(primarch_dates[2])
            segmento.add_planet(planeta)
            if len(self.__primarchs) == 20:
                print('RuntimeError: There can only be 20 Primarchs')
            else:
                self.__primarchs.append(Primarch(primarch_dates[0], planeta, primarch_dates[1], Status.ALIVE, self))

    @property
    def primarchs(self) -> list['Primarch']:
        return self.__primarchs

    @property
    def name(self) -> str:
        return self.__name

    def add_bureaucrat(self, bureaucrat: 'Bureaucrat') -> None:
        self.__administratum.add_bureaucrat(bureaucrat)

    @property
    def planet(self) -> 'Planet':
        return self.__planet

    @classmethod
    def get_instance(cls):
        if cls.__INSTANCE is None:
            raise SingletonError(f'There is no {cls.__name__} instance')
        return cls.__INSTANCE

    def get_bureaucrat(self, index: int) -> 'Bureaucrat':
        return self.__administratum.bureaucrats[index]
    

    def register_planet(self, bureaucrat: 'Bureaucrat', planet: dict) -> None:
        planeta = self.crear_planeta(planet)
        if planeta == self.__administratum.planet_registry[-1]:
            print('RuntimeError: Planet already registered')
        else:
            new_segmento = self.crear_segmentum(planet).add_planet(planeta)
            self.__administratum.planet_registry.append(planeta)
            self.__administratum.planet_registry[self.__administratum.buscar_bureaucrat(bureaucrat)] +=1
            self.__administratum.planet_registry.pop(-1)
            self.__administratum.planet_registry.append(planeta)

    def add_regiment(self, name: str, planet: str) -> None:
        info_planet = {
            'planet_name': planet,
            'planet_type': 'planet'
        }
        planeta = self.crear_planeta(info_planet)
        self.__astra_militarum.add_regiment(Regiment(name, planeta))

    def get_regiment(self, index: int) -> 'Regiment':
        return self.__astra_militarum.regiment_index(index)

    def bureaucrat_max_registry(self) -> list['Bureaucrat', int]:
        registry_buro = {}
        for i in range(len(self.__administratum.bureaucrats)):
            registry_buro[self.__administratum.bureaucrats[i]] = self.__administratum.planet_registry[i]
    
        return [max(registry_buro, key=registry_buro.get), max(registry_buro.values())]
         
    def planet_type_quantity(self) -> None:
        planets = []
        
        for segmento in self.__segmentums:
            planets.extend(segmento.planets)
        for planeta in planets:
            if planeta.type_ == PlanetType.HIVE :
                planets.remove(planeta)
                break
        planet_type = {}
        for planet in planets:
            if planet.type_ in planet_type:
                planet_type[planet.type_] += 1
            else:
                planet_type[planet.type_] = 1
        planet_type2 = dict(sorted(planet_type.items(), key=lambda x: x[0].value))

        print('---------- Planet Type ----------')
        for llave, valor in planet_type2.items():
            print(f'- {llave.value} Planet Quantity = {valor}')
 
    def show_primarchs_summary(self) -> None:
        def generar_numero_romano(numero):
            valores = {
                1000: 'M',
                900: 'CM',
                500: 'D',
                400: 'CD',
                100: 'C',
                90: 'XC',
                50: 'L',
                40: 'XL',
                10: 'X',
                9: 'IX',
                5: 'V',
                4: 'IV',
                1: 'I'
            }
            for valor, simbolo in valores.items():
                while numero >= valor:
                    yield simbolo
                    numero -= valor
        print('\n---------- Primarchs Summary ----------')
        posicion = 0
        for primarch in self.__primarchs:
            posicion += 1
            posicion_romano = ''.join(generar_numero_romano(posicion))
            if primarch is None:
                print(f'- Primarch '+ posicion_romano)
                print(f'  - Purged from Imperial Registry')
                print('\n')
            else:
                print(f'- Primarch '+ posicion_romano)
                print(f'  - ID: {primarch.id_string}')
                print(f'  - Name: {primarch.name}')
                print(f'  - Alias: {primarch.alias}')
                print(f'  - Loyal: {primarch.loyalty}')
                print(f'  - Status: {primarch.status.value}')
                print(f'  - Planet: {primarch.planet.nombre}')
                print(f'    - Astra Militarum Regiments Quantity: {len(primarch.planet.regiments)}')
                soldiers = 0
                for regiment in primarch.planet.regiments:
                    soldiers += len(regiment.soldiers)
                print(f'    - Astra Militarum Total Soldiers: {soldiers}')
                for chapter in self.__adeptus_astarte.chapters:
                    if chapter.primarch == primarch:
                        print(f'    - Adeptus Astates Chapter: {chapter.name}')
                        break
                print(f'      - Successor Chapters:')
                for chapter in self.__adeptus_astarte.chapters:
                    for successor in chapter.successor_chapters:
                        if successor.primarch == primarch:
                            print(f'        - {successor.name}')
                print('\n')