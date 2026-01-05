# **Oefening: Dierentuinbeheersysteem**

Je krijgt de opdracht om een dierentuinbeheersysteem te ontwerpen dat informatie beheert over verschillende soorten dieren, hun dieet, leefomgeving en verzorgers. De dierentuin heeft allerlei soorten dieren met elk hun eigen kenmerken en gedrag. Het systeem moet in staat zijn om dieren in categorieën te organiseren, hun voedselbehoefte te berekenen, hun gezondheid bij te houden en rapporten te genereren.

---

## **Vereisten**

### Deel 1: Abstracte Dierklasse

1. Definieer een abstracte klasse **`Dier`**:

   * Constructorparameters:

     1. **`naam`**: Een string die de naam van het dier voorstelt.
     2. **`leeftijd`**: Een geheel getal dat de leeftijd van het dier aangeeft.
     3. **`soort`**: Een string die de soort van het dier aanduidt.
   * Maak publieke attributen voor `naam`, `leeftijd` en `soort`.
   * Definieer privé-attributen:

     1. **`gezondheid`**: Een geheel getal (van 0 tot 100) dat de gezondheid van het dier bijhoudt.
     2. **`voedselbehoefte`**: Een float die de dagelijkse voedselbehoefte in kilogram voorstelt.
   * Voeg een eigenschap **`gezondheid`** toe:

     * Getter: Retourneert de gezondheidswaarde van het dier.
     * Setter: Werkt de gezondheid bij en zorgt ervoor dat deze tussen 0 en 100 blijft.
   * Voeg een eigenschap **`voedselbehoefte`** toe:

     * Getter: Retourneert de dagelijkse voedselbehoefte.
     * Setter: Werkt de voedselbehoefte bij en zorgt ervoor dat deze positief blijft.
   * Implementeer een abstracte methode **`bereken_voedselbehoefte()`**:

     * Subklassen moeten deze methode implementeren op basis van soort en leeftijd.
   * Implementeer een abstracte methode **`genereer_rapport()`**:

     * Deze methode geeft een gedetailleerd rapport over naam, leeftijd, soort, gezondheid en voedselbehoefte van het dier.

---

### Deel 2: Subklassen van Dier

#### **2.1 Zoogdier**

* Definieer een klasse **`Zoogdier`** die erft van `Dier`:

  * Constructorparameter:

    1. **`vacht_type`**: Een string die het type vacht beschrijft (bijv. "kort", "lang").
  * Sla `vacht_type` op als publiek attribuut.
  * Override **`bereken_voedselbehoefte()`**:

    * Zoogdieren hebben een voedselbehoefte van:
      $\text{voedselbehoefte} = \text{leeftijd} \times 0.5\ \text{(in kg)}$
  * Override **`genereer_rapport()`**:

    * Voeg `vacht_type` toe aan het rapport.

#### **2.2 Vogel**

* Definieer een klasse **`Vogel`** die erft van `Dier`:

  * Constructorparameter:

    1. **`vleugelspanwijdte`**: Een float die de vleugelspanwijdte in meters aangeeft.
  * Sla `vleugelspanwijdte` op als publiek attribuut.
  * Override **`bereken_voedselbehoefte()`**:

    * Vogels hebben een voedselbehoefte van:
      $\text{voedselbehoefte} = \text{leeftijd} \times 0.2\ \text{(in kg)}$
  * Override **`genereer_rapport()`**:

    * Voeg `vleugelspanwijdte` toe aan het rapport.

#### **2.3 Reptiel**

* Definieer een klasse **`Reptiel`** die erft van `Dier`:

  * Constructorparameter:

    1. **`is_giftig`**: Een boolean die aanduidt of het reptiel giftig is.
  * Sla `is_giftig` op als publiek attribuut.
  * Override **`bereken_voedselbehoefte()`**:

    * Reptielen hebben een voedselbehoefte van:
      $\text{voedselbehoefte} = \text{leeftijd} \times 0.3\ \text{(in kg)}$
  * Override **`genereer_rapport()`**:

    * Voeg toe of het reptiel giftig is.

---

### Deel 3: Zoo Klasse

Definieer een klasse **`Dierentuin`**:

1. Constructorparameters:

   * **`naam`**: Een string die de naam van de dierentuin voorstelt.
   * **`locatie`**: Een string die de locatie van de dierentuin voorstelt.
2. Attributen:

   * Sla `naam` en `locatie` op als publieke attributen.
   * Gebruik een privé lijst `_dieren` om alle dieren in de dierentuin op te slaan.
3. Implementeer een methode **`voeg_dier_toe(dier)`**:

   * Voegt een `Dier` toe aan de dierentuin.
   * Geeft een `TypeError` als het argument geen instantie van `Dier` is.
4. Implementeer een methode **`verwijder_dier(dier_naam)`**:

   * Verwijdert een dier op basis van zijn naam.
   * Geeft een `ValueError` als het dier niet bestaat.
5. Implementeer een methode **`bereken_totale_voeding()`**:

   * Retourneert de totale dagelijkse voedselbehoefte van alle dieren.
6. Implementeer een methode **`genereer_dierentuin_rapport()`**:

   * Genereert een rapport met:

     * De naam en locatie van de dierentuin.
     * Het totaal aantal dieren.
     * Een individueel rapport voor elk dier.

---

### Deel 4: Geavanceerde Functionaliteit

#### **4.1 Gezondheidscontrole**

Implementeer een methode **`controleer_dier_gezondheid(drempel)`** in de klasse `Dierentuin`:

* Vindt en lijst alle dieren met een gezondheidswaarde onder de opgegeven drempel.

#### **4.2 Dieren Categoriseren**

Implementeer een methode **`categoriseer_dieren()`** in de klasse `Dierentuin`:

* Categoriseert dieren op basis van soort en retourneert een woordenboek.

#### **4.3 Seizoensgebonden Voedingsaanpassing**

Voeg een methode toe **`pas_voeding_aan_voor_seizoen(seizoen)`**:

* In de winter: verhoog de voedselbehoefte voor zoogdieren met 20%.
* In de zomer: verlaag de voedselbehoefte voor reptielen met 10%.
* Laat de voedselbehoefte voor vogels onveranderd.

---

### Voorbeeldgebruik

```python
# Maak dieren aan
leeuw = Zoogdier("Leeuw", 5, "Panthera leo", "kort")
papegaai = Vogel("Papegaai", 2, "Psittacidae", 0.25)
python_slang = Reptiel("Python", 3, "Pythonidae", True)

# Bereken voedselbehoefte
leeuw.bereken_voedselbehoefte()
papegaai.bereken_voedselbehoefte()
python_slang.bereken_voedselbehoefte()

# Genereer individuele rapporten
print(leeuw.genereer_rapport())
print(papegaai.genereer_rapport())
print(python_slang.genereer_rapport())

# Maak een dierentuin aan
dierentuin = Dierentuin("Safari Dierentuin", "Californië")

# Voeg dieren toe aan de dierentuin
dierentuin.voeg_dier_toe(leeuw)
dierentuin.voeg_dier_toe(papegaai)
dierentuin.voeg_dier_toe(python_slang)

# Genereer dierentuinrapport
print(dierentuin.genereer_dierentuin_rapport())

# Controleer dieren met lage gezondheid
dieren_met_lage_gezondheid = dierentuin.controleer_dier_gezondheid(drempel=50)
print(dieren_met_lage_gezondheid)

# Categoriseer dieren
categorieën = dierentuin.categoriseer_dieren()
print(categorieën)

# Pas voeding aan voor de winter
dierentuin.pas_voeding_aan_voor_seizoen("winter")
print(dierentuin.genereer_dierentuin_rapport())
```
