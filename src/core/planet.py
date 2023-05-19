



class Planet:
    def __init__(self, name: str, type_: 'PlanetType', chapter: 'Chapter' = None,
                 regiments: list['Regiment'] = None) -> None:
        self.__name = name
        self.__type_ = type_
        self.__chapter = chapter
        self.__regiments = regiments if regiments else []

    @property
    def nombre(self) -> str:
        return self.__name

    def add_chapter(self, chapter: 'Chapter') -> None:
        self.__chapter = chapter

    def add_regiment(self,regiment: 'Regiment') -> None:
        self.__regiments.append(regiment)

    @property
    def chapter(self) -> 'Chapter':
        return self.__chapter

    @property
    def regiments(self) -> list['Regiment']:
        return self.__regiments


