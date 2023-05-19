



class Planet:
    def __init__(self, name: str, type_: 'PlanetType', chapter: 'Chapter' = None,
                 regiments: list['Regiment'] = None) -> None:
        self.__name = name
        self.__type_ = type_
        self.__chapter = chapter
        self.__regiments = regiments if regiments else []
        for regiment in self.__regiments:
            regiment.add_planet(self)

    @property
    def nombre(self) -> str:
        return self.__name

    def add_chapter(self, chapter: 'Chapter') -> None:
        self.__chapter = chapter

    @property
    def chapter(self) -> 'Chapter':
        return self.__chapter

    @property
    def regiments(self) -> list['Regiment']:
        return self.__regiments


