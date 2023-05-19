from src.core.emperor import *
from src.enumeration.enumeration import *
from src.person.person import *


def main() -> None:
    try:
        emperor = Emperor()
        fake_emperor = Emperor()
    except SingletonError as ex:
        print(f'{ex.__class__.__name__}: {ex}')

    terra_info = {
        'planet_name': 'Terra',
        'planet_type': PlanetType.HIVE,
        'segmentum_name': 'Solar',
        'segmentum_location': 'Center'
    }

    emperor.create_imperium('The Imperium of Mankind', terra_info)  # If the planet or segmentum is not created it must be created

    planets_info = {
        'caliban': {
            'planet_name': 'Caliban',
            'planet_type': PlanetType.FEUDAL,
            'segmentum_name': 'Obscurus',
            'segmentum_location': 'North'
        },
        'chemos': {
            'planet_name': 'Chemos',
            'planet_type': PlanetType.CIVILISED,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'olympia': {
            'planet_name': 'Olympia',
            'planet_type': PlanetType.CIVILISED,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'chogoris': {
            'planet_name': 'Chogoris',
            'planet_type': PlanetType.FEUDAL,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'fenris': {
            'planet_name': 'Fenris',
            'planet_type': PlanetType.DEATH,
            'segmentum_name': 'Obscurus',
            'segmentum_location': 'North'
        },
        'terra': terra_info,
        'nostramo': {
            'planet_name': 'Nostramo',
            'planet_type': PlanetType.HIVE,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'baal': {
            'planet_name': 'Baal',
            'planet_type': PlanetType.DEATH,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'medusa': {
            'planet_name': 'Medusa',
            'planet_type': PlanetType.FERAL,
            'segmentum_name': 'Obscurus',
            'segmentum_location': 'North'
        },
        'nuceria': {
            'planet_name': 'Nuceria',
            'planet_type': PlanetType.CIVILISED,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'macragge': {
            'planet_name': 'Macragge',
            'planet_type': PlanetType.CIVILISED,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'barbarus': {
            'planet_name': 'Barbarus',
            'planet_type': PlanetType.DEATH,
            'segmentum_name': 'Tempestus',
            'segmentum_location': 'South'
        },
        'prospero': {
            'planet_name': 'Prospero',
            'planet_type': PlanetType.CIVILISED,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'cthonia': {
            'planet_name': 'Cthonia',
            'planet_type': PlanetType.FERAL,
            'segmentum_name': 'Solar',
            'segmentum_location': 'Center'
        },
        'colchis': {
            'planet_name': 'Colchis',
            'planet_type': PlanetType.FEUDAL,
            'segmentum_name': 'Pacificus',
            'segmentum_location': 'West'
        },
        'nocturne': {
            'planet_name': 'Nocturne',
            'planet_type': PlanetType.DEATH,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'deliverance': {
            'planet_name': 'Deliverance',
            'planet_type': PlanetType.DEAD,
            'segmentum_name': 'Tempestus',
            'segmentum_location': 'South'
        },
        'cadia': {
            'planet_name': 'Cadia',
            'planet_type': PlanetType.DAEMON,
            'segmentum_name': 'Obscurus',
            'segmentum_location': 'North'
        },
        'mars': {
            'planet_name': 'Mars',
            'planet_type': PlanetType.FORGE,
            'segmentum_name': 'Solar',
            'segmentum_location': 'Center'
        },
        'armageddon': {
            'planet_name': 'Armageddon',
            'planet_type': PlanetType.HIVE,
            'segmentum_name': 'Solar',
            'segmentum_location': 'Center'
        },
        'catachan': {
            'planet_name': 'Catachan',
            'planet_type': PlanetType.DEATH,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'krieg': {
            'planet_name': 'Krieg',
            'planet_type': PlanetType.DEATH,
            'segmentum_name': 'Tempestus',
            'segmentum_location': 'South'
        },
        'aexe': {
            'planet_name': 'Aexe Cardinal',
            'planet_type': PlanetType.AGRI,
            'segmentum_name': 'Pacificus',
            'segmentum_location': 'West'
        },
        'spectoris': {
            'planet_name': 'Spectoris',
            'planet_type': PlanetType.AGRI,
            'segmentum_name': 'Obscurus',
            'segmentum_location': 'North'
        },
        'kaggeran': {
            'planet_name': 'Kaggeran',
            'planet_type': PlanetType.FRONTIER,
            'segmentum_name': 'Ultima',
            'segmentum_location': 'East'
        },
        'vaxanide': {
            'planet_name': 'Vaxanide',
            'planet_type': PlanetType.FRONTIER,
            'segmentum_name': 'Obscurus',
            'segmentum_location': 'North'
        }
    }

    imperium = Imperium.get_instance()

    # The id_string of a person must be a 6 character hexadecimal string generated sequentially
    # The name of a person must be the name sent by parameter plus the id_string generated
    emperor.create_primarch('Lion El Jonson', 'The Lion', planets_info['caliban'])  # If the planet or segmentum is not created it must be created.
    emperor.create_primarch(None)  # If there is no info, a None must be added to Primarchs list.
    emperor.create_primarch('Fulgrim', 'The Phoenician', planets_info['chemos'])
    emperor.create_primarch('Perturabo', 'Lord of Iron', planets_info['olympia'])
    emperor.create_primarch('Jaghatai Khan', 'The Warhawk', planets_info['chogoris'])
    emperor.create_primarch('Leman Russ', 'Wolf King', planets_info['fenris'])
    emperor.create_primarch('Rogal Dorn', 'Praetorian of Terra', planets_info['terra'])  # The planet is already created, so no message is shown
    emperor.create_primarch('Konrad Curze', 'Night Haunter', planets_info['nostramo'])
    emperor.create_primarch('Sanguinius', 'Great Angel', planets_info['baal'])
    emperor.create_primarch('Ferrus Manus', 'The Gorgon', planets_info['medusa'])
    emperor.create_primarch(None)
    emperor.create_primarch('Angron', 'Red Angel', planets_info['nuceria'])
    emperor.create_primarch('Roboute Guilliman', 'The Blade of Unity', planets_info['macragge'])
    emperor.create_primarch('Mortarion', 'Pale King', planets_info['barbarus'])
    emperor.create_primarch('Magnus the Red', 'Crimson King', planets_info['prospero'])
    emperor.create_primarch('Horus Lupercal', 'The Warmaster', planets_info['cthonia'])
    emperor.create_primarch('Lorgar Aurelian', 'The First Heretic', planets_info['colchis'])
    emperor.create_primarch('Vulkan', 'The Promethean Flame', planets_info['nocturne'])
    emperor.create_primarch('Corvus Corax', 'Raven Lord', planets_info['deliverance'])
    emperor.create_primarch('Alpharius Omegon', 'Last Primarch', planets_info['cadia'])
    emperor.create_primarch('Belisarius Cawl', 'The Archimagus', planets_info['mars'])  # The Primarch can't be added, but planet is added

    imperium.primarchs[2].betray()
    imperium.primarchs[3].betray()
    imperium.primarchs[7].betray()
    imperium.primarchs[11].betray()
    imperium.primarchs[13].betray()
    imperium.primarchs[14].betray()
    imperium.primarchs[15].betray()
    imperium.primarchs[16].betray()
    imperium.primarchs[19].betray()

    imperium.primarchs[4].change_status(Status.UNKNOWN)
    imperium.primarchs[5].change_status(Status.UNKNOWN)
    imperium.primarchs[6].change_status(Status.UNKNOWN)
    imperium.primarchs[7].change_status(Status.DEAD)
    imperium.primarchs[8].change_status(Status.DEAD)
    imperium.primarchs[9].change_status(Status.DEAD)
    imperium.primarchs[15].change_status(Status.DEAD)
    imperium.primarchs[16].change_status(Status.UNKNOWN)
    imperium.primarchs[17].change_status(Status.UNKNOWN)
    imperium.primarchs[18].change_status(Status.UNKNOWN)
    imperium.primarchs[19].change_status(Status.UNKNOWN)

    imperium.add_bureaucrat(Bureaucrat('Imperial Bureaucrat', 'Departmento Munitorum', planets_info['terra']))  # A new registry must be added at Administratum with value 0
    imperium.register_planet(imperium.get_bureaucrat(0), planets_info['armageddon'])  # The registry must increase in 1
    imperium.register_planet(imperium.get_bureaucrat(0), planets_info['armageddon'])  # The registry mustn't increase
    imperium.register_planet(imperium.get_bureaucrat(0), planets_info['catachan'])

    imperium.add_chapter('Dark Angels', imperium.primarchs[0], 'Caliban')
    imperium.add_chapter('Emperor Children', imperium.primarchs[2], 'Chemos')
    imperium.add_chapter('Iron Warriors', imperium.primarchs[3], 'Olympia')
    imperium.add_chapter('White Scars', imperium.primarchs[4], 'Chogoris')
    imperium.add_chapter('Space Wolves', imperium.primarchs[5], 'Fenris')
    imperium.add_chapter('Imperial Fists', imperium.primarchs[6], 'Terra')
    imperium.add_chapter('Night Lords', imperium.primarchs[7], 'Nostramo')
    imperium.add_chapter('Blood Angels', imperium.primarchs[8], 'Baal')
    imperium.add_chapter('Iron Hands', imperium.primarchs[9], 'Medusa')
    imperium.add_chapter('World Eaters', imperium.primarchs[11], 'Nuceria')
    imperium.add_chapter('Ultramarines', imperium.primarchs[12], 'Macragge')
    imperium.add_chapter('Death Guard', imperium.primarchs[13], 'Barbarus')
    imperium.add_chapter('Thousand Sons', imperium.primarchs[14], 'Prospero')
    imperium.add_chapter('Sons of Horus', imperium.primarchs[15], 'Cthonia')
    imperium.add_chapter('Word Bearers', imperium.primarchs[16], 'Colchis')
    imperium.add_chapter('Salamanders', imperium.primarchs[17], 'Nocturne')
    imperium.add_chapter('Raven Guard', imperium.primarchs[18], 'Deliverance')
    imperium.add_chapter('Alpha Legion', imperium.primarchs[19], 'Cadia')
    imperium.add_chapter('Black Consuls', imperium.primarchs[12], 'Armageddon')
    imperium.get_chapter(10).add_successor_chapter(imperium.get_chapter(-1))

    for i in range(1001):
        imperium.get_chapter(10).add_astarte(Astarte('Space Marine', (i % 10) + 1, planets_info['macragge']))  # Must show an error message on 1001 astarte

    imperium.add_bureaucrat(Bureaucrat('Imperial Bureaucrat', 'Officio Medicae', planets_info['terra']))
    imperium.register_planet(imperium.get_bureaucrat(1), planets_info['krieg'])
    imperium.register_planet(imperium.get_bureaucrat(1), planets_info['aexe'])
    imperium.register_planet(imperium.get_bureaucrat(1), planets_info['spectoris'])

    imperium.add_regiment('Death Korps of Krieg 1st Siege Army', 'Krieg')
    for i in range(300):
        imperium.get_regiment(0).add_soldier(Soldier('Imperial Guardsman', (i % 10) + 16, planets_info['krieg']))
    print(f'Registered {len(imperium.get_regiment(0).soldiers)} Soldiers in {imperium.get_regiment(0).name}')

    imperium.add_regiment('Honor Guard of Macragge 1st Infantry Army', 'Macragge')
    for i in range(210):
        imperium.get_regiment(1).add_soldier(Soldier('Imperial Guardsman', (i % 10) + 16, planets_info['macragge']))
    print(f'Registered {len(imperium.get_regiment(1).soldiers)} Soldiers in {imperium.get_regiment(1).name}')

    imperium.add_regiment('Honor Guard of Macragge 2nd Infantry Army', 'Macragge')
    for i in range(130):
        imperium.get_regiment(2).add_soldier(Soldier('Imperial Guardsman', (i % 10) + 16, planets_info['macragge']))
    print(f'Registered {len(imperium.get_regiment(2).soldiers)} Soldiers in {imperium.get_regiment(2).name}')

    imperium.add_bureaucrat(Bureaucrat('Imperial Bureaucrat', 'Logis Strategos', planets_info['terra']))
    imperium.register_planet(imperium.get_bureaucrat(2), planets_info['kaggeran'])
    imperium.register_planet(imperium.get_bureaucrat(2), planets_info['vaxanide'])

    print(
        f'The {imperium.bureaucrat_max_registry()[0].name} has the maximum registry '
        f'with {imperium.bureaucrat_max_registry()[1]} Planets\n'
    )

    imperium.planet_type_quantity()
    imperium.show_primarchs_summary()


if __name__ == '__main__':
    main()

""" RESULTS
The Emperor of Mankind has arisen
SingletonError: There can only be one Emperor of Mankind
Added Planet Terra to Segmentum Solar
The Emperor created The Imperium of Mankind at planet Terra
Added Segmentum Solar to the Imperium
Added Segmentum Obscurus to the Imperium
Added Planet Caliban to Segmentum Obscurus
The Emperor created Primarch Lion El Jonson
The Emperor created Primarch *****
Added Segmentum Ultima to the Imperium
Added Planet Chemos to Segmentum Ultima
The Emperor created Primarch Fulgrim
Added Planet Olympia to Segmentum Ultima
The Emperor created Primarch Perturabo
Added Planet Chogoris to Segmentum Ultima
The Emperor created Primarch Jaghatai Khan
Added Planet Fenris to Segmentum Obscurus
The Emperor created Primarch Leman Russ
The Emperor created Primarch Rogal Dorn
Added Planet Nostramo to Segmentum Ultima
The Emperor created Primarch Konrad Curze
Added Planet Baal to Segmentum Ultima
The Emperor created Primarch Sanguinius
Added Planet Medusa to Segmentum Obscurus
The Emperor created Primarch Ferrus Manus
The Emperor created Primarch *****
Added Planet Nuceria to Segmentum Ultima
The Emperor created Primarch Angron
Added Planet Macragge to Segmentum Ultima
The Emperor created Primarch Roboute Guilliman
Added Segmentum Tempestus to the Imperium
Added Planet Barbarus to Segmentum Tempestus
The Emperor created Primarch Mortarion
Added Planet Prospero to Segmentum Ultima
The Emperor created Primarch Magnus the Red
Added Planet Cthonia to Segmentum Solar
The Emperor created Primarch Horus Lupercal
Added Segmentum Pacificus to the Imperium
Added Planet Colchis to Segmentum Pacificus
The Emperor created Primarch Lorgar Aurelian
Added Planet Nocturne to Segmentum Ultima
The Emperor created Primarch Vulkan
Added Planet Deliverance to Segmentum Tempestus
The Emperor created Primarch Corvus Corax
Added Planet Cadia to Segmentum Obscurus
The Emperor created Primarch Alpharius Omegon
Added Planet Mars to Segmentum Solar
RuntimeError: There can only be 20 Primarchs
Primarch Fulgrim betrays the Emperor
Primarch Perturabo betrays the Emperor
Primarch Konrad Curze betrays the Emperor
Primarch Angron betrays the Emperor
Primarch Mortarion betrays the Emperor
Primarch Magnus the Red betrays the Emperor
Primarch Horus Lupercal betrays the Emperor
Primarch Lorgar Aurelian betrays the Emperor
Primarch Alpharius Omegon betrays the Emperor
Imperial Bureaucrat 000013 started to work at Imperium
Added Planet Armageddon to Segmentum Solar
RuntimeError: Planet already registered
Added Planet Catachan to Segmentum Ultima
Created Chapter Dark Angels of Adeptus Astartes
Created Chapter Emperor Children of Adeptus Astartes
Created Chapter Iron Warriors of Adeptus Astartes
Created Chapter White Scars of Adeptus Astartes
Created Chapter Space Wolves of Adeptus Astartes
Created Chapter Imperial Fists of Adeptus Astartes
Created Chapter Night Lords of Adeptus Astartes
Created Chapter Blood Angels of Adeptus Astartes
Created Chapter Iron Hands of Adeptus Astartes
Created Chapter World Eaters of Adeptus Astartes
Created Chapter Ultramarines of Adeptus Astartes
Created Chapter Death Guard of Adeptus Astartes
Created Chapter Thousand Sons of Adeptus Astartes
Created Chapter Sons of Horus of Adeptus Astartes
Created Chapter Word Bearers of Adeptus Astartes
Created Chapter Salamanders of Adeptus Astartes
Created Chapter Raven Guard of Adeptus Astartes
Created Chapter Alpha Legion of Adeptus Astartes
Created Chapter Black Consuls of Adeptus Astartes
Added Successor Chapter Black Consuls to Chapter Ultramarines
Chapter Ultramarines is full
RuntimeError: There can only be 1000 Astartes per Chapter
Imperial Bureaucrat 0003fd started to work at Imperium
Added Planet Krieg to Segmentum Tempestus
Added Planet Aexe Cardinal to Segmentum Pacificus
Added Planet Spectoris to Segmentum Obscurus
Created Regiment Death Korps of Krieg 1st Siege Army of Astra Militarum
Registered 300 Soldiers in Death Korps of Krieg 1st Siege Army
Created Regiment Honor Guard of Macragge 1st Infantry Army of Astra Militarum
Registered 210 Soldiers in Honor Guard of Macragge 1st Infantry Army
Created Regiment Honor Guard of Macragge 2nd Infantry Army of Astra Militarum
Registered 130 Soldiers in Honor Guard of Macragge 2nd Infantry Army
Imperial Bureaucrat 00067e started to work at Imperium
Added Planet Kaggeran to Segmentum Ultima
Added Planet Vaxanide to Segmentum Obscurus
The Imperial Bureaucrat 0003fd has the maximum registry with 3 Planets

---------- Planet Type ----------
- Agri Planet Quantity = 2
- Civilised Planet Quantity = 5
- Daemon Planet Quantity = 1
- Dead Planet Quantity = 1
- Death Planet Quantity = 6
- Feral Planet Quantity = 2
- Feudal Planet Quantity = 3
- Forge Planet Quantity = 1
- Frointer Planet Quantity = 2
- Hive Planet Quantity = 3

---------- Primarchs Summary ----------
- Primarch I
  - ID: 000000
  - Name: Lion El Jonson
  - Alias: The Lion
  - Loyal: True
  - Status: Alive
  - Planet: Caliban
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Dark Angels
      - Successor Chapters:

- Primarch II
  - Purged from Imperial Registry

- Primarch III
  - ID: 000001
  - Name: Fulgrim
  - Alias: The Phoenician
  - Loyal: False
  - Status: Alive
  - Planet: Chemos
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Emperor Children
      - Successor Chapters:

- Primarch IV
  - ID: 000002
  - Name: Perturabo
  - Alias: Lord of Iron
  - Loyal: False
  - Status: Alive
  - Planet: Olympia
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Iron Warriors
      - Successor Chapters:

- Primarch V
  - ID: 000003
  - Name: Jaghatai Khan
  - Alias: The Warhawk
  - Loyal: True
  - Status: Unknown
  - Planet: Chogoris
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: White Scars
      - Successor Chapters:

- Primarch VI
  - ID: 000004
  - Name: Leman Russ
  - Alias: Wolf King
  - Loyal: True
  - Status: Unknown
  - Planet: Fenris
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Space Wolves
      - Successor Chapters:

- Primarch VII
  - ID: 000005
  - Name: Rogal Dorn
  - Alias: Praetorian of Terra
  - Loyal: True
  - Status: Unknown
  - Planet: Terra
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Imperial Fists
      - Successor Chapters:

- Primarch VIII
  - ID: 000006
  - Name: Konrad Curze
  - Alias: Night Haunter
  - Loyal: False
  - Status: Dead
  - Planet: Nostramo
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Night Lords
      - Successor Chapters:

- Primarch IX
  - ID: 000007
  - Name: Sanguinius
  - Alias: Great Angel
  - Loyal: True
  - Status: Dead
  - Planet: Baal
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Blood Angels
      - Successor Chapters:

- Primarch X
  - ID: 000008
  - Name: Ferrus Manus
  - Alias: The Gorgon
  - Loyal: True
  - Status: Dead
  - Planet: Medusa
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Iron Hands
      - Successor Chapters:

- Primarch XI
  - Purged from Imperial Registry

- Primarch XII
  - ID: 000009
  - Name: Angron
  - Alias: Red Angel
  - Loyal: False
  - Status: Alive
  - Planet: Nuceria
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: World Eaters
      - Successor Chapters:

- Primarch XIII
  - ID: 00000a
  - Name: Roboute Guilliman
  - Alias: The Blade of Unity
  - Loyal: True
  - Status: Alive
  - Planet: Macragge
    - Astra Militarum Regiments Quantity: 2
    - Astra Militarum Total Soldiers: 340
    - Adeptus Astates Chapter: Ultramarines
      - Successor Chapters:
        - Black Consuls

- Primarch XIV
  - ID: 00000b
  - Name: Mortarion
  - Alias: Pale King
  - Loyal: False
  - Status: Alive
  - Planet: Barbarus
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Death Guard
      - Successor Chapters:

- Primarch XV
  - ID: 00000c
  - Name: Magnus the Red
  - Alias: Crimson King
  - Loyal: False
  - Status: Alive
  - Planet: Prospero
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Thousand Sons
      - Successor Chapters:

- Primarch XVI
  - ID: 00000d
  - Name: Horus Lupercal
  - Alias: The Warmaster
  - Loyal: False
  - Status: Dead
  - Planet: Cthonia
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Sons of Horus
      - Successor Chapters:

- Primarch XVII
  - ID: 00000e
  - Name: Lorgar Aurelian
  - Alias: The First Heretic
  - Loyal: False
  - Status: Unknown
  - Planet: Colchis
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Word Bearers
      - Successor Chapters:

- Primarch XVIII
  - ID: 00000f
  - Name: Vulkan
  - Alias: The Promethean Flame
  - Loyal: True
  - Status: Unknown
  - Planet: Nocturne
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Salamanders
      - Successor Chapters:

- Primarch XIX
  - ID: 000010
  - Name: Corvus Corax
  - Alias: Raven Lord
  - Loyal: True
  - Status: Unknown
  - Planet: Deliverance
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Raven Guard
      - Successor Chapters:

- Primarch XX
  - ID: 000011
  - Name: Alpharius Omegon
  - Alias: Last Primarch
  - Loyal: False
  - Status: Unknown
  - Planet: Cadia
    - Astra Militarum Regiments Quantity: 0
    - Astra Militarum Total Soldiers: 0
    - Adeptus Astates Chapter: Alpha Legion
      - Successor Chapters:

"""