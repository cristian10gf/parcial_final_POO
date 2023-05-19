from src.person.primarch import Primarch
from src.person.person import Planet


class Segmentum:
    def __init__(self, name: str, location: str, planet: list['Planet']) -> None:
        self.__name = name
        self.__location = location
        self.__planets = planet
        

    @property
    def name(self) -> str:
        return self.__name

    @property
    def planets(self) -> list['Planet']:
        return self.__planets

    def add_planet(self, planet: Planet) -> None:
        self.__planets.append(planet)
        print(f'Added Planet {planet.nombre} to Segmentum {self.__name}')

    def planet_id(self,name: str)-> 'Planet':
        for planet in self.__planets:
            if planet.nombre == name:
                return planet


class AstraMilitarum:
    def __init__(self) -> None:
        self.__regiments: list['Regiment'] = []

    def add_regiment(self, regiment: 'Regiment') -> None:
        self.__regiments.append(regiment)
    
    def regiment_index(self, index: int) -> 'Regiment':
        return self.__regiments[index]


class Regiment:
    def __init__(self, name: str, planet: Planet) -> None:
        self.__name = name
        self.__planet = planet

        self.__soldiers: list['Soldier'] = []
        planet.add_regiment(self)
        print(f'Created Regiment {self.name} of Astra Militarum')

    @property
    def name(self) -> str:
        return self.__name

    @property
    def planet(self) -> Planet:
        return self.__planet

    @property
    def soldiers(self) -> list['Soldier']:
        return self.__soldiers

    def add_soldier(self, soldier: 'Soldier') -> None:
        self.__soldiers.append(soldier)


class Administratum:
    def __init__(self) -> None:
        self.__planet_registry: list[int] = []
        self.__bureaucrats: list['Bureaucrat'] = []

    @property
    def bureaucrats(self) -> list['Bureaucrat']:
        return self.__bureaucrats

    @property
    def planet_registry(self) -> list[int]:
        return self.__planet_registry

    def add_bureaucrat(self, bureaucrat: 'Bureaucrat') -> None:
        new_registry  = []
        for registry in self.__planet_registry:
            if isinstance(registry, int):
                new_registry.append(registry)

        self.__planet_registry = new_registry

        self.__planet_registry.append(0)
        self.__bureaucrats.append(bureaucrat)
        print(f'{bureaucrat.name} {bureaucrat.id_string} started to work at Imperium')

    def buscar_bureaucrat(self, bureaucrat: 'Bureaucrat') -> int:
        pos = 0
        for bureaucrat_regis in self.__bureaucrats:
            if bureaucrat_regis.id_string == bureaucrat.id_string:
                return pos
            else:
                pos += 1


class Chapter:
    def __init__(self, name: str, primarch: Primarch, planet: Planet) -> None:
        self.__name = name
        self.__primarch = primarch
        self.__planet = planet
        self.__astartes: list['Astarte'] = []
        self.__successor_chapters: list['Chapter'] = []
        planet.add_chapter(self)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def primarch(self) -> Primarch:
        return self.__primarch

    @property
    def planet(self) -> Planet:
        return self.__planet

    @property
    def astartes(self) -> list['Astarte']:
        return self.__astartes

    @property
    def successor_chapters(self) -> list['Chapter']:
        return self.__successor_chapters
    
    def add_astarte(self, astarte: 'Astarte') -> None:
        if len(self.__astartes) == 1000:
            print(f'{self.name} is full')
            print(f'RuntimeError: There can only be 1000 Astartes per Chapter')
        else:
            self.__astartes.append(astarte)

    def add_successor_chapter(self, chapter: 'Chapter')-> None:
        self.__successor_chapters.append(chapter)
        print(f'Added Successor Chapter {chapter.name} to Chapter {self.name}')


class AdeptusAstartes:
    def __init__(self, chapter: list['Chapter'] = None) -> None:
        self.__chapters = chapter if chapter else []

    def add_chapter(self, chapter: Chapter) -> None:
        self.__chapters.append(chapter)
        print(f'Created Chapter {chapter.name} of Adeptus Astartes')

    def get_chapter(self, index: int) -> Chapter:
        return self.__chapters[index]

