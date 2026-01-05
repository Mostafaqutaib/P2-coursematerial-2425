# **Exercise logger-app**

Bekijk de startcode (in `starter_code.py`). Dit is een deel van de implementatie van een nieuwe oefenlogger-app die we aan het ontwikkelen zijn.

In deze applicatie kunnen we drie types oefeningen loggen: `Run`, `Ride` en `Swim`. Deze drie klassen hebben een aantal zaken gemeen:

* Velden:

  * `date`
  * `distance`
  * `duration`
* Methoden/properties:

  * `is_valid_date`
  * `calories`

Toch hebben deze drie klassen ook hun verschillen:

* `Run` en `Ride` houden ook een elevation factor bij; `Swim` (uiteraard) niet.
* Hoewel de `calories`-property voor alle klassen bestaat, wordt de property `calories_factor` op een andere manier berekend.

---

## **Belangrijk: Vermijd code duplicatie**

In deze opdracht verwachten we dat je je oplossing implementeert op een manier die overbodige code duplicatie vermijdt, door gebruik te maken van de principes die je dit semester geleerd hebt.

---

## **Kopieer de code**

Maak een kopie van de startcode in het bestand `student.py`. Implementeer alle onderstaande vragen in dit bestand.

---

## **Vraag 1: Refactor de code**

Zoals je ziet, hebben de klassen `Run`, `Swim` en `Ride` gemeenschappelijke elementen, ondanks hun verschillen. Maak in het nieuwe bestand `student.py` een geschikte abstracte klasse `Exercise` en herstructureer `Run`, `Swim` en `Ride` zodat ze erven van deze `Exercise`-klasse. Vermijd hierbij zoveel mogelijk code duplicatie. Gebruik waar nodig abstracte methoden of properties om af te dwingen dat elke subklasse zijn eigen implementatie biedt voor gedrag dat verschilt.

> Tip: Onderaan het bestand vind je voorbeeldcode. Gebruik deze om te controleren of jouw wijzigingen de werking van de applicatie niet breken.

---

## **Vraag 2: Operator overloading**

Zodra we oefeningen hebben aangemaakt, willen we ook de effectiviteit van elke oefening met elkaar kunnen vergelijken. Zorg ervoor dat oefensessies met elkaar vergeleken kunnen worden op basis van verbrande calorieën, zoals in het voorbeeld hieronder:

```python
>>> morning_run = Run("2023-10-02", 5, 21, 12)
>>> morning_run.calories
800
>>> evening_bike_ride = Ride("2023-10-01", 20, 60, 0)
>>> evening_bike_ride.calories
800
>>> morning_run == evening_bike_ride
True
>>> morning_run < evening_bike_ride
False
>>> morning_run > evening_bike_ride
False
```

---

## **Vraag 3: static method**

Voor één van de methoden in de code is het geschikter om deze om te zetten naar een static method. Zet deze methode om naar een static method en pas de rest van de code aan zodat alles correct blijft werken.

---

## **Vraag 4: `is_valid_date`**

De huidige implementatie van `is_valid_date` kan verbeterd worden. Gebruik een enkele regex-string om deze methode compacter te maken.

---

## **Vraag 5: Comprehensions**

Gebruik **list comprehensions** om de volgende methoden te implementeren:

* Een methode `filter(self, condition)` in de klasse `ExerciseLog`, die een lijst teruggeeft van `Exercise`-objecten die voldoen aan een bepaalde voorwaarde.
* Een methode `filter_by_date(self, date)` die een lijst teruggeeft van `Exercise`-objecten waarvan de `date` overeenkomt met de opgegeven `date`.
* Een methode `filter_by_distance(self, min_distance)` die een lijst teruggeeft van `Exercise`-objecten waarvan de `distance` minstens gelijk is aan de parameter `min_distance`.

---

## **Vraag 6: testen**

Schrijf tests voor de klasse `Swim`.

* Voor de constructor:

  * Test minstens één succesvolle creatie van een `Swim`-object.
  * Test dat in de juiste gevallen exceptions worden opgegooid.
* Schrijf een **geparameteriseerde test** voor de `calories`-property.
