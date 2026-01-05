# **Werknemerssysteem Project**

Bij de opdracht **Werknemersbeheersysteem** is het doel om werknemersgegevens te beheren en verschillende werknemersgerelateerde handelingen uit te voeren (zoals aannemen, ontslaan, gegevens bijwerken, enz.) met behulp van OOP-concepten (Objectgeoriënteerd Programmeren).

Het systeem bestaat uit drie hoofdklassen:

1. **Werknemer (Employee)**
2. **WerknemersManager (EmployeesManager)**
3. **FrontendManager**

Elke klasse moet in een apart bestand worden geïmplementeerd, en het systeem moet functioneel zijn wanneer het hoofdscript wordt uitgevoerd. De klassen moeten de principes van objectgeoriënteerd programmeren volgen en naadloos kunnen samenwerken om werknemers te beheren. Er wordt niet veel informatie gegeven om mee te starten — het is aan jou om uit te zoeken hoe je dit systeem programmeert.

---

## Inhoudsopgave

* [Inleiding](#inleiding)
* [Klassen](#klassen)

  * [Werknemer](#werknemer)
  * [WerknemersManager](#werknemersmanager)
  * [FrontendManager](#frontendmanager)

---

## Inleiding

Het **Werknemerssysteem Project** toont de implementatie van objectgeoriënteerde programmeerconcepten in Python. Het omvat drie hoofdklassen, elk met een eigen doel:

### 🧑‍💼 Werknemer (Employee)

De `Werknemer`-klasse vertegenwoordigt een individuele werknemer met de volgende attributen:

* `naam`: De naam van de werknemer.
* `leeftijd`: De leeftijd van de werknemer.
* `salaris`: Het salaris van de werknemer.

Deze klasse biedt methoden voor een stringrepresentatie en geformatteerde uitvoer van werknemersinformatie.

---

### WerknemersManager (EmployeesManager)

De `WerknemersManager`-klasse is verantwoordelijk voor het beheren van een lijst met werknemers. Deze biedt functionaliteiten om:

* Een nieuwe werknemer toe te voegen aan de lijst.
* Alle bestaande werknemers weer te geven.
* Werknemers te verwijderen binnen een opgegeven leeftijdsbereik.
* Een werknemer te zoeken op naam.
* Het salaris van een werknemer bij te werken op basis van de naam.

---

### FrontendManager

De `FrontendManager`-klasse biedt een gebruikersinterface om te communiceren met de `WerknemersManager`. Gebruikers kunnen acties uitvoeren zoals:

* Nieuwe werknemers toevoegen.
* Bestaande werknemers weergeven.
* Werknemers verwijderen op basis van een leeftijdsbereik.
* Salarissen van werknemers bijwerken op basis van hun naam.

