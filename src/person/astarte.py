from src.person.person import Person, Planet


class Astarte(Person):
    def __init__(self, name: str, founding: int, planet: 'Planet' or dict) -> None:
        planet = Planet(planet['planet_name'],planet['planet_type'])
        super().__init__(name, planet)
        self.__founding = founding


    @property
    def founding(self) -> int:
        return self.__founding
