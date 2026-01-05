## Examenvraag: Ticketsysteem voor Evenementen

* Plaats alle code voor deze oefening in `ticketing.py`.
* In deze instructies vermelden we `self` niet expliciet.
  Jij moet weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen exact correct gebruikt, inclusief de parameternamen.

### Util

* Definieer een klasse `Util`.
* Definieer een statische methode `is_valid_ticket_id(ticket_id)` die `True` retourneert als de ticket\_id geldig is, anders `False`. Controleer dit met behulp van een reguliere expressie.

  * Een ticket\_id bestaat uit exact 10 tekens.
  * Een ticket\_id begint altijd met TICK.
  * Daarna volgen 4 cijfers tussen 1000 en 9999.
  * Vervolgens komen er 2 hoofdletters.
  * Voorbeelden: "TICK1234AB" en "TICK5678CD" zijn geldige ticket\_id’s, maar "TICK0123AB" en "TICK56789EF" zijn ongeldig.

### Ticket

* Definieer een klasse `Ticket`.
* Definieer de constructor van `Ticket`.

  * De constructor neemt drie parameters: `ticket_id` (string), `event_name` (string), en `price` (float).
  * Als een instantie van `Ticket` wordt gemaakt met een ongeldige ticket\_id, moet er een `ValueError` worden opgegooid.
* Sla `event_name` en `price` op in publieke velden.
* Sla `ticket_id` op in een privéveld en maak deze toegankelijk via een property.

  * Definieer een getter en een setter voor `ticket_id`.
* Voeg de `dunder method` toe om een leesbare stringrepresentatie van het ticketobject te bieden.

  * Deze functie moet de volgende uitvoer produceren: `Ticket: "event_name", Price: "price", Ticket ID: "ticket_id"`
  * Voorbeeld:

    * "Ticket: Live Concert, Price: 99.99, Ticket ID: TICK5678AB"

### Event

Een `Event` stelt een verzameling tickets voor. Er bestaan verschillende soorten evenementen, maar alle evenementen delen enkele gemeenschappelijke kenmerken. Daarom definiëren we een abstracte klasse `Event` om deze gemeenschappelijke eigenschappen op te slaan.

* Definieer een abstracte klasse `Event`.
* Definieer een constructor voor `Event`.

  * Deze heeft twee parameters: `name` (string), `max_tickets` (int).
  * Sla deze op in *publieke* velden.
  * Voeg een *privéveld* `tickets` toe om een dictionary van alle beschikbare tickets voor dit event op te slaan.

    * De keys van deze dictionary zijn de ticket\_id’s.
    * De values zijn de ticketobjecten.
  * Wanneer een `Event` wordt aangemaakt, zijn er nog geen tickets toegevoegd.
* Definieer een read-only property `sold_tickets` die het aantal verkochte tickets voor dit `Event` retourneert.
* Definieer een read-only property `available_tickets` die het resterende aantal tickets voor dit `Event` retourneert.

  * Dit wordt berekend door `sold_tickets` af te trekken van `max_tickets`.
* Definieer een methode `add_ticket(ticket)` om een `Ticket` toe te voegen aan de `tickets` dictionary.

  * Wanneer het aantal tickets het maximum overschrijdt, moet deze methode een `RunTimeError` geven.
* Definieer een methode `remove_ticket(ticket)` om een `Ticket` te verwijderen uit de `tickets` dictionary.

  * Als het ticket dat verwijderd moet worden niet in de dictionary zit, geeft deze methode een `RunTimeError`.
* Definieer een property `ticket_prices` die een lijst van prijzen (floats) van alle tickets in dit `Event` retourneert.

  * Gebruik List Comprehension hiervoor.
* Definieer een methode `sort_tickets_by_price` die een lijst retourneert van tickets gesorteerd op prijs (hoog naar laag) met behulp van een lambda-functie.
* Definieer een abstracte methode `create_event_summary()`.

### Soorten Evenementen

Zoals eerder vermeld, zijn er verschillende soorten evenementen: Concert, Conference, SportsEvent, enz. De gemeenschappelijke functionaliteit is al geïmplementeerd in `Event`. Hieronder definiëren we twee subclasses: `Concert` en `Conference`.

#### `Concert`

Een `Concert` erft van `Event`.

* Definieer een constructor voor `Concert`.

  * Deze heeft twee parameters, geërfd van de constructor van `Event`.
  * Voeg nog een extra publiek veld toe: `performers` (een lijst van strings).
* Implementeer `create_event_summary`

  * Deze functie retourneert een string met de samenvatting van het evenement.
  * De string bevat:

    * De naam van het concert
    * De artiesten van het concert
    * De tickets van het concert (één regel per ticket), gesorteerd op prijs van hoog naar laag

      * Elke regel bevat: ticket\_id gevolgd door de prijs en de event\_name.
    * Zie voorbeeldgebruik hieronder.

#### `Conference`

Een `Conference` erft van `Event`.

* Definieer een constructor voor `Conference`.

  * Deze heeft één parameter: `name`, geërfd van de constructor van `Event`.
  * Het aantal `max_tickets` is altijd gelijk aan 500.
* Implementeer `create_event_summary`

  * Deze functie retourneert een string met de samenvatting van het evenement.
  * De string bevat:

    * De naam van de conferentie
    * De tickets van de conferentie (één regel per ticket), gesorteerd op prijs van hoog naar laag

      * Elke regel bevat: ticket\_id gevolgd door de prijs en de event\_name.
* Implementeer de methode `add_ticket(ticket)`:

  * Door de aard van een conferentie mogen enkel tickets met een prijs van maximaal 300.00 worden toegevoegd.
  * Indien een ticket met een hogere prijs wordt toegevoegd, moet een `RunTimeError` worden opgegooid.

---

### Voorbeeldgebruik

```python
# Maak enkele tickets aan
>>> vip_ticket = Ticket("TICK1234AB", "VIP Concert", 299.99)
>>> regular_ticket = Ticket("TICK5678CD", "Live Concert", 99.99)
>>> conference_ticket = Ticket("TICK2345EF", "Tech Conference", 150.00)
>>> invalid_ticket = Ticket("TICK6789GH", "Sports Event", 75.00)
ValueError: Ongeldige Ticket ID opgegeven
>>> premium_conference_ticket = Ticket("TICK3456IJ", "Tech Conference", 350.00)

# Print VIP Ticket
>>> print(vip_ticket)
Ticket: "VIP Concert", Price: 299.99, Ticket ID: TICK1234AB

# Maak een concert aan
>>> rock_concert = Concert("Rock Fest", 500, ["Band A", "Band B", "Band C"])

# Voeg tickets toe aan het concert
>>> rock_concert.add_ticket(vip_ticket)
>>> rock_concert.add_ticket(regular_ticket)

# Print ticketprijzen
>>> print(rock_concert.ticket_prices)
[299.99, 99.99]

# Print samenvatting van het evenement
>>> print(rock_concert.create_event_summary())
Event: Rock Fest  
Performers: Band A, Band B, Band C  
TICK1234AB - 299.99 (VIP Concert)  
TICK5678CD - 99.99 (Live Concert)

# Maak een conferentie aan
>>> tech_conference = Conference("Tech Innovations")

# Voeg tickets toe aan de conferentie
>>> tech_conference.add_ticket(conference_ticket)
>>> tech_conference.add_ticket(premium_conference_ticket)
RuntimeError: Tickets duurder dan 300.00 mogen niet worden toegevoegd aan een Conference

# Print samenvatting van de conferentie
>>> print(tech_conference.create_event_summary())
Event: Tech Innovations  
TICK2345EF - 150.00 (Tech Conference)
```

---

### Testing

Je moet tests schrijven die de methode `create_event_summary` voldoende testen. Plaats deze tests in het bestand `test-ticketing.py`.

* Raadpleeg de beschrijvingen van `Concert` en `Conference` om te weten hoe je `create_event_summary` moet implementeren.
* Gebruik de conventies uit het hoofdstuk over testen om deze functionaliteit te testen.
