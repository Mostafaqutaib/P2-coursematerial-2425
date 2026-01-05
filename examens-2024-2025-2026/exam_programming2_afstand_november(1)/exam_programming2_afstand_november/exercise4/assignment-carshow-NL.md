# Examen Vraag 1: Carshow

* Plaats alle code voor deze oefening in `carshow.py`.
* In deze instructies laten we altijd het vermelden van `self` achterwege.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen precies goed hebt, zelfs die van de parameters.
* Je hebt een bestand `basic_tests.py` ontvangen dat basis testen bevat, zoals of bepaalde klassen bestaan en of je de juiste namen hebt gebruikt.
  * Voer deze tests uit met het commando:

    ```bash
    $ pytest basic_tests.py
    ```

  * Een ontbrekende klasse zorgt ervoor dat tests die zich richten op die klasse worden overgeslagen.
    Overgeslagen tests tellen daarom nog steeds als mislukt.
  * De tests voeren alleen oppervlakkige controles uit.
    Falende/overgeslagen tests betekenen dat je code zeker onvolledig of incorrect is.
    Maar geslaagde tests betekenen niet dat je code volledig correct is!
* Je moet ook zelf enkele tests maken in het bestand `test-carshow.py`.
  * Alle tests die je zelf moet schrijven, zijn aangegeven in dit opdrachtbestand.
  * Je kunt hier extra tests aan toevoegen als je je code grondiger wilt controleren. Alleen de tests die in de opdracht worden gevraagd, worden beoordeeld.
  * Dit testbestand moet correct kunnen worden uitgevoerd om punten te verdienen.

## Util

* Definieer een klasse `Util`.
* Definieer een statische methode `is_valid_license_plate(license_plate)` die `True` retourneert als de license_plate op basis van een reguliere expressie geldig is en anders `False`.
  * Een license_plate bestaat uit 3 delen.
    * Het eerste deel bestaat uit het cijfer 1 of 2
    * Het tweede deel bestaat uit drie hoofdletters, van AAA tot ZZZ
    * Het derde deel bestaat uit drie cijfers, van 111 tot 999
  * De drie delen in een license_plate worden door een koppelteken (-) gescheiden.
  * Voorbeelden: "2-BFQ-223", "1-LUV-368" en "1-ABC-123" zijn geldige license_plates, maar "3-XYZ-456", "2-123-ABC" en "1-Gta-276" niet.

## Car

Er zijn verschillende soorten cars, maar alle cars delen enkele gemeenschappelijke kenmerken. Daarom zullen we een abstracte klasse `Car` definiëren om gemeenschappelijke kenmerken van verschillende soorten cars op te slaan.

* Definieer abstracte een klasse `Car`.
* Definieer de constructor van `Car`.
  * De constructor neemt drie parameters: `license_plate` (een string), `color` (een string), `amount_wheels` (een int).
  * Wanneer er een instantie van een `Car` aangemaakt wordt met een ongeldige license_plate, moet er een ValueError gegenereerd worden.
* Sla `color` en `amount_wheels` op in opbenbare velden.
* Sla `license_plate` op in een privéveld en maak het toegankelijk via een eigenschap.
  * Definieer een getter en een setter voor `license_plate`.
* Definieer een abstracte methode `get_price()`.

## Soorten Cars

Zoals eerder vermeld, zijn er verschillende soorten cars: Supercars, Sedans, Trucks, etc...
Gemeenschappelijke functionaliteit is al geïmplementeerd in `Car`. Hieronder zullen we twee dergelijke subklassen definiëren om onderscheid te maken tussen soorten cars. Om te voorkomen dat dit examen te lang wordt, zullen we alleen `Supercar` en `Truck` implementeren.

### `Supercar`

Een `Supercar` erft van `Car`.

* Definieer een constructor voor `Supercar`.
  * Het heeft drie parameters
    * `license_plate` en `color` zijn overgenomen van de `Car` constructor.
      * De amount of wheels van een supercar is steeds gelijk aan 4.
    * De andere parameter, `top_speed`, is een integer.
      * Bewaar `top_speed` als een openbaar veld.
* Implementeer `get_price`
  * Bereken de prijs van deze Supercar:
  * De prijs bereken je door 500 te vermenigvuldigen met de top speed gedeeld door het aantal wielen.

### `Truck`

Een `Truck` erft van `Car`.

* Definieer een constructor voor `Truck`.
  * Het heeft vier parameters
    * `license_plate`, `color` and `amount_wheels` zijn overgenomen van de `Car` constructor.
    * De andere parameter, `weight_of_load`, is een integer.
      * Bewaar `weight_of_load` als een openbaar veld.
* Implementeer `get_price`
  * Bereken de prijs van deze Truck:
  * De kosten bereken je door 25 te vermenigvuldigen met de weight of load gedeeld door het aantal wielen.

### `Car (bis)`

* Voeg de `dunder methode` toe om een leesbare string representatie te geven van het car object
  * Wanneer deze functie aangeroepen wordt, wordt de volgende output gemaakt indien het een supercar is: `License Plate: "license_plate", Color: "color", Amount of Wheels: "amount_wheels", Top Speed: "top_speed"`
  * Wanneer deze functie aangeroepen wordt, wordt de volgende output gemaakt indien het een truck is: `License Plate: "license_plate", Color: "color", Amount of Wheels: "amount_wheels", Weight of Load: "weight_of_load"`
  * Voorbeelden:
    * print(mclarenp1)
    * "License Plate: 2-BFQ-223, Color: Orange, Amount of Wheels: 4, Top Speed: 350"
    * print(scania)
    * "License Plate: 1-ABC-123, Color: Blue, Amount of Wheels: 8, Weight of Load: 32000"

## Carshow

Een `Carshow` vertegenwoordigt een carshow waarin meerdere cars zitten.

* Definieer een klasse `Carshow`.
* Definieer een constructor voor `Carshow`.
  * Het heeft drie parameters: `name` (een string), `halls` (een int), `spots` (een int).
  * Sla deze op in *openbare* velden.
  * Voeg nog een *privaat* veld `cars` toe om een lijst van alle cars die in de carshow zitten, op te slaan.
    * De values van deze lijst zijn de car objecten
  * Bij aanmaak heeft een `Carshow` geen geregistreerde cars.
* Definieer een alleen-lezen eigenschap `number_of_cars` die het aantal geregistreerde `cars` voor deze `Carshow` retourneert.
* Definieer een methode `add_car(car)` om een ​​`Car` aan de `cars` lijst toe te voegen.
  * Wanneer het maximaal aantal cars reeds bereikt is, genereert deze methode een `RunTimeError`.
  * Het maximaal aantal cars toegelaten is het aantal halls vermenigvuldigd met het aantal spots.
* Definieer een methode `remove_car(car)` om een `Car` uit de `cars` lijst te verwijderen.
  * Wanneer de te verwijderen car niet in de lijst zit, genereert deze methode een `RunTimeError`.
* Definieer een eigenschap `car_license_plates` die een lijst met license plates (strings) van alle cars die in deze `Carshow` zitten, retourneert.
  * Maak hiervoor gebruik van List Comprehension.
* Defineer een methode `sort_cars_by_license_plate` die aan de hand van een lambda functie een lijst teruggeeft van cars, oplopend gesorteert op license plate.
* Definieer een methode `get_total_price()`.
  * Geeft de totale prijs terug van de carshow door de som te nemen van de individuele prijs van elke car.

## Voorbeeldgebruik

```python
# enkele cars aanmaken
>>> mclarenp1 = Supercar("2-BFQ-223", "Orange", 350)
>>> bugattichiron = Supercar("1-LUV-368", "Black", 420)
>>> faulty_car = Supercar("1-Gta-276", "Green" , 10)
ValueError("Invalid license plate provided")
>>> scania = Truck("1-ABC-123", "Blue", 8, 32000)
>>> iveco = Truck("2-IVE-400", "White", 10, 40000)
>>> dactrucks = Truck("1-DAC-440", "Yellow", 12, 44000)

# Sportcar uitprinten
>>> print(mclarenp1)
License Plate: 2-BFQ-223, Color: Orange, Amount of Wheels: 4, Top Speed: 350
# Truck uitprinten
>>> print(scania)
License Plate: 1-ABC-123, Color: Blue, Amount of Wheels: 8, Weight of Load: 32000

# Calculating the price of a car
>>> print(bugattichiron.get_price())
52500.0
>>> print(iveco.get_price())
100000.0

# Making a Carshow
>>> ucll_carshow = Carshow("UCLL Carshow", 1, 3)

# Adding some cars to the carshow
>>> ucll_carshow.add_car(mclarenp1)
>>> ucll_carshow.add_car(bugattichiron)
>>> ucll_carshow.add_car(scania)
>>> ucll_carshow.add_car(dactrucks)
RuntimeError("The carshow is full")
>>> ucll_carshow.remove_car(iveco)
RuntimeError("Car was not in the carshow")
>>> ucll_carshow.remove_car(scania)
>>> ucll_carshow.add_car(dactrucks)

# Carshow methods & properties
>>> print(ucll_carshow.number_of_cars)
3
>>> print(ucll_carshow.car_license_plates)
['2-BFQ-223', '1-LUV-368', '1-DAC-440']

>>> print(ucll_carshow.get_total_price())
187916.6666666667
```

# Testing
Je moet tests schrijven die voldoende de eigenschap `get_price` testen. Neem deze tests op in het bestand `test-carshow.py`.

* Raadpleeg de beschrijving van zowel `Supercar` als `Truck` voor informatie over hoe je `get_price` kunt implementeren.
* Gebruik de conventies die je hebt geleerd in het hoofdstuk over Testen om deze functionaliteit te kunnen testen.