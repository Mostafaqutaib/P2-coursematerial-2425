# Examen Vraag 2: Gaming Inventory System

* Plaats alle code voor deze oefening in `inventory.py`.
* In deze instructies laten we telkens `self` weg.
  Het is aan jou om te weten wanneer je deze extra parameter moet toevoegen.
* Zorg ervoor dat je de namen exact correct gebruikt, inclusief de parameter-namen.

---

## Util

* Definieer een klasse `Util`.
* Definieer een statische methode `is_valid_item_id(item_id)` die `True` teruggeeft als de `item_id` geldig is, anders `False`. Controleer dit met een **reguliere expressie**.

  * Een `item_id` bestaat uit exact 9 karakters.
  * Een `item_id` begint altijd met `ITM`.
  * Daarna volgt een 4-cijferig getal tussen 1000 en 9999.
  * Tot slot volgen er 2 hoofdletters.
  * Voorbeelden: `"ITM1234AB"` en `"ITM5678CD"` zijn geldig, maar `"ITM0123B"` en `"ITM56789EF"` niet.

---

## Item

* Definieer een klasse `Item`.
* Definieer de constructor van `Item`.

  * De constructor neemt drie parameters: `item_id` (string), `name` (string) en `value` (float).
  * Wanneer een instantie van `Item` wordt aangemaakt met een ongeldige `item_id`, moet er een `ValueError` opgegooid worden.
* Sla `name` en `value` op in **publieke velden**.
* Sla `item_id` op in een **privé veld** en maak dit toegankelijk via een property.
* Voeg de `dunder method` toe zodat het object een leesbare stringrepresentatie krijgt.

  * Voorbeeld:

    * `"Item: Sword of Power, Value: 499.99, Item ID: ITM1234AB"`

---

## Inventory

Een `Inventory` stelt een collectie van game-items voor. Er bestaan verschillende types inventories (afhankelijk van het spel), maar alle inventories hebben gemeenschappelijke eigenschappen. Daarom definiëren we een **abstracte klasse `Inventory`** waarin de basisfunctionaliteit zit.

* Definieer een abstracte klasse `Inventory`.
* Definieer de constructor van `Inventory`.

  * Hij neemt twee parameters: `owner` (string), `max_items` (int).
  * Sla deze op in **publieke velden**.
  * Voeg een **privé veld** `items` toe om een dictionary bij te houden met alle items in dit inventory.

    * De keys zijn de `item_id`s.
    * De values zijn de item-objecten.
  * Bij het aanmaken heeft een `Inventory` nog geen items.
* Definieer een **read-only property** `stored_items` die het aantal items in het inventory teruggeeft.
* Definieer een **read-only property** `available_space` die weergeeft hoeveel items er nog kunnen worden toegevoegd.
* Definieer een methode `add_item(item)` die een `Item` toevoegt aan de `items` dictionary.

  * Als het aantal items het maximum overschrijdt, moet er een `RunTimeError` opgegooid worden.
* Definieer een methode `remove_item(item)` die een `Item` uit de `items` dictionary verwijdert.

  * Als het item niet aanwezig is, moet er een `RunTimeError` opgegooid worden.
* Definieer een property `item_values` die een lijst teruggeeft van de waarden van alle items.
* Definieer een methode `sort_items_by_value` die een lijst van items teruggeeft, gesorteerd op waarde (hoog naar laag).
* Definieer een abstracte methode `create_inventory_summary()`.

---

## Types of Inventories

We definiëren twee subklassen: `PlayerInventory` en `GuildInventory`.

### `PlayerInventory`

Een `PlayerInventory` erft over van `Inventory`.

* Definieer de constructor van `PlayerInventory`.

  * Hij neemt twee parameters over van `Inventory`.
  * Voeg daarnaast een publiek veld `character_class` toe (string, bv. `"Mage"`, `"Warrior"`).
* Implementeer `create_inventory_summary`:

  * De samenvatting moet bevatten:

    * De naam van de speler (`owner`).
    * De character class.
    * De lijst van items (één regel per item), gesorteerd op waarde (hoog naar laag).

      * Elke regel: `item_id - value (name)`

---

### `GuildInventory`

Een `GuildInventory` erft over van `Inventory`.

* Definieer de constructor van `GuildInventory`.

  * Hij heeft één parameter: `owner`, overgenomen van `Inventory`.
  * Het `max_items` van een `GuildInventory` is altijd gelijk aan 1000.
* Implementeer `create_inventory_summary`:

  * De samenvatting moet bevatten:

    * De naam van de guild (`owner`).
    * De lijst van items (gesorteerd op waarde hoog → laag).
* Implementeer de methode `add_item(item)`:

  * Enkel items met een waarde ≤ `1000.00` mogen toegevoegd worden.
  * Als een duurder item wordt toegevoegd, moet er een `RunTimeError` opgegooid worden.

---

## Voorbeeldgebruik

```python
# Maak enkele items aan
>>> sword = Item("ITM1234AB", "Sword of Power", 499.99)
>>> potion = Item("ITM5678CD", "Health Potion", 29.99)
>>> guild_banner = Item("ITM2345EF", "Guild Banner", 750.00)
>>> invalid_item = Item("ITM789GH", "Broken Shield", 15.00)
ValueError: Invalid Item ID provided
>>> legendary_artifact = Item("ITM3456IJ", "Legendary Artifact", 5000.00)

# Print Sword
>>> print(sword)
Item: Sword of Power, Value: 499.99, Item ID: ITM1234AB

# Maak een PlayerInventory
>>> mage_inventory = PlayerInventory("Arthas", 20, "Mage")

# Voeg items toe
>>> mage_inventory.add_item(sword)
>>> mage_inventory.add_item(potion)

# Print item values
>>> print(mage_inventory.item_values)
[499.99, 29.99]

# Print inventory summary
>>> print(mage_inventory.create_inventory_summary())
Player: Arthas (Class: Mage)
ITM1234AB - 499.99 (Sword of Power)
ITM5678CD - 29.99 (Health Potion)

# Maak een GuildInventory
>>> guild_inventory = GuildInventory("Knights of Valor")

# Voeg items toe
>>> guild_inventory.add_item(guild_banner)
>>> guild_inventory.add_item(legendary_artifact)
RuntimeError: Items valued above 1000.00 cannot be added to a GuildInventory

# Print guild summary
>>> print(guild_inventory.create_inventory_summary())
Guild: Knights of Valor
ITM2345EF - 750.00 (Guild Banner)
```