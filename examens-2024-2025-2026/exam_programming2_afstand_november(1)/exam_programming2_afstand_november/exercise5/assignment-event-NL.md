# Examen Vraag 1: Events

* Plaats alle code voor deze oefening in `event.py`.
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
* Je moet ook zelf enkele tests maken in het bestand `test-event.py`.
  * Alle tests die je zelf moet schrijven, zijn aangegeven in dit opdrachtbestand.
  * Je kunt hier extra tests aan toevoegen als je je code grondiger wilt controleren. Alleen de tests die in de opdracht worden gevraagd, worden beoordeeld.
  * Dit testbestand moet correct kunnen worden uitgevoerd om punten te verdienen.

## Util

* Definieer een klasse `Util`.
* Definieer een statische methode `is_valid_sabam_id(sabam_id)` die `True` retourneert als de sabam_id geldig is en anders `False`. Controleer dit door gebruik te maken van een reguliere expressie.
  * Een sabam_id bestaat uit exact 12 characters
  * Een sabam_id begint altijd met SB
  * Hierna volgen er 6 willekeurige cijfers
  * Tot slot volgen er 4 klinkers die in hoofdletter staan
  * Voorbeelden: "SB123456AEIO" en "SB112233AAEE" zijn geldige sabam_id's, maar "SB12345AAAA" en "SB123456AZER" niet.

## Artiest (Artist)

* Definieer een klasse `Artist`.
* Definieer de constructor van `Artist`.
  * De constructor neemt drie parameters: `sabam_id` (een string), `name` (een string) en `wage` (een int).
  * De constructor moet een `ValueError` genereren als de sabam_id ongeldig is.
* Sla `name` en `wage` op in openbare velden.
* Sla `sabam_id` op in een privéveld en maak het toegankelijk via een eigenschap (property).
  * Definieer een getter en een setter voor `sabam_id`.
* Voeg de `dunder methode` toe om een leesbare string representatie te geven van het artiest-object
  * Wanneer deze functie aangeroepen wordt, wordt de volgende output gemaakt: `Artist: "artist_name", Wage: "artist_wage", Sabam ID: "artist_sabam_id"`
  * Voorbeeld: "Artist: Rihanna, Wage: 20000, Sabam ID: SB123456AAAA"

## Event

Een `Event` vertegenwoordigt een event waar artiesten komen optreden op verschillende podia en gedurende verschillende speelslots. Er zijn verschillende soorten events, maar alle events delen enkele gemeenschappelijke kenmerken. Daarom zullen we een abstracte klasse `Event` definiëren om gemeenschappelijke kenmerken van verschillende soorten events op te slaan.

* Definieer een abstracte klasse `Event`.
* Definieer een constructor voor `Event`.
  * Het heeft drie parameters: `name` (een string), `number_of_stages` (een int) en `number_of_slots` (een int) .
  * Sla deze op in *openbare* velden.
  * Voeg nog een *privaat* veld `artists` toe om een ​​dictionary van alle artiesten die op dit event spelen, op te slaan.
  * Bij aanmaak heeft een `Event` geen geregistreerde artiesten.
* Definieer een alleen-lezen eigenschap (property) `number_of_artists` die het aantal geregistreerde `artiesten` voor dit `Event` retourneert.
* Definieer een alleen-lezen eigenschap `maximum_artists` die het maximaal aantal geregistreerde `artiesten` voor dit `Event` retourneert.
  * Het maximaal aantal geregistreerde artiesten krijg je door het aantal podia te vermenigvuldigen met het aantal speelslots.
* Definieer een methode `add_artist(artist)` om een ​​`Artist` aan de `artists` dictionary toe te voegen.
  * Wanneer het maximaal aantal artiesten reeds bereikt is, genereert deze methode een `RunTimeError`.
* Definieer een methode `remove_Artist(artist)` om een `Artist` uit de `artists` dictionary te verwijderen.
  * Wanneer de te verwjderen artiest niet in de dictionary zit, genereert deze methode een `RunTimeError`.
* Definieer een eigenschap (property) `sum_wages_of_artists` die de som van de wages van alle artiesten die op dit `Event` spelen, retourneert.
  * Maak hiervoor gebruik van List Comprehension.
* Defineer een methode `sort_artists_by_name` die aan de hand van een lambda functie een lijst teruggeeft van artiesten, gesorteerd op naam (laag naar hoog).
* Definieer een abstracte methode `calculate_profit()`.

## Soorten Events

Zoals eerder vermeld, zijn er verschillende soorten events: Festival, Concert, FreeConcert, etc...
Gemeenschappelijke functionaliteit is al geïmplementeerd in `Event`. Hieronder zullen we twee dergelijke subklassen definiëren om onderscheid te maken tussen soorten events. Om te voorkomen dat dit examen te lang wordt, zullen we alleen `Festival` en `FreeConcert` implementeren.

### `Festival`

Een `Festival` erft (inherits) van `Event`.

* Definieer een constructor voor `Festival`.
  * Het heeft drie parameters: alle drie overgenomen van de constructor van `Event`.
  * Voeg een ander openbaar veld `number_of_attendees`(een int) toe.
  * Voeg een ander openbaar veld `ticket_price`(een int) toe.
* Implementeer `calculate_profit`
  * Bereken de winst van dit Festival: opbrengst - kosten
  * De opbrengst bereken je door het aantal aanwezigen te vermenigvuldigen met de ticket prijs
  * De kosten bereken je door de lonen van alle aanwezige artiesten op te tellen

### `FreeConcert`

Een `FreeConcert` erft (inherits) van `Event`.

* Definieer een constructor voor `FreeConcert`.
  * Het heeft twee parameters: `name` en `number_of_slots`, beide overgenomen van de constructor van `Event`.
  * Het aantal podia voor een FreeConcert is steeds gelijk aan 1.
* Implementeer `calculate_profit`
  * Bereken de winst van dit FreeConcert: opbrengst - kosten
  * De opbrengst van een gratis concert is gelijk aan 0
  * De kosten bereken je door de lonen van alle aanwezige artiesten op te tellen
* Implementeer de methode `add_artist(artist)`:
  * Op een FreeConcert komen enkel artiesten met een loon onder de 10000 euro
  * Indien een artiest toegevoegd wordt die meer wil verdienen, genereert deze methode een `RunTimeError`


## Voorbeeldgebruik

```python
# creating some artists
>>> rihanna = Artist("SB123456AAAA", "Rihanna", 20000)
>>> camille = Artist("SB123456BBBB", "Camille", 5000)
ValueError("Invalid Sabam ID provided")
>>> metallica = Artist("SB123456EEEE", "Metallica", 30000)
>>> pommelien = Artist("SB123456OOOO", "Pommelien Thijs", 5000)
>>> samson = Artist("SB123456IIII", "Samson en Gert", 8000)
>>> elton = Artist("SB123456UUUU", "Elton John", 22000)
>>> elvis = Artist("SB123455AAAA", "Elvis Presley", 50000)

# printing Rihanna
>>> print(rihanna)
Artist: Rihanna, Wage: 20000, Sabam ID: SB123456AAAA

# creating a Festival
>>> rock_werchter = Festival("Rock Werchter", 1, 2, 10000, 10)

# adding some artists to the festival
>>> rock_werchter.add_artist(metallica)
>>> rock_werchter.add_artist(rihanna)
>>> rock_werchter.add_artist(samson)
RuntimeError("Line-up Full. Cannot add artist")
>>> rock_werchter.remove_artist(rihanna)
>>> rock_werchter.add_artist(samson)
>>> rock_werchter.remove_artist(elvis)
RuntimeError("Artist was not in the line-up")

# Print Artist names sorted
>>> sorted_artists = rock_werchter.sort_artists_by_name()
>>> for artist in sorted_artists:
>>>     print(artist)
Artist: Rihanna, Wage: 20000, Sabam ID: SB123456AAAA
Artist: Metallica, Wage: 30000, Sabam ID: SB123456EEEE
Artist: Samson en Gert, Wage: 8000, Sabam ID: SB123456IIII

# calculating the profit of Rock Werchter
>>> print(rock_werchter.calculate_profit())
62000

# creating a FreeConcert
>>> rock_blanden = FreeConcert("Rock Blanden", 1)

# adding some artists to Rock Blanden
>>> rock_blanden.add_artist(elton)
RuntimeError("Artist too expensive to play on a free concert")
>>> rock_blanden.add_artist(pommelien)

# calculating the profit (loss) of Rock Blanden
>>> print(rock_blanden.calculate_profit())
-5000
```

# Testing
Je moet tests schrijven die voldoende de eigenschap `calculate_profit` testen. Neem deze tests op in het bestand `test-event.py`.

* Raadpleeg de beschrijving van zowel `Festival` als `FreeConcert` voor informatie over hoe je `calculate_profit` kunt implementeren.
* Gebruik de conventies die je hebt geleerd in het hoofdstuk over Testen om deze functionaliteit te kunnen testen.
