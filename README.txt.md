# Voetbalcompetitie

In deze oefening gaan we een Python-script schrijven dat een bestand zoals `match_data.txt` kan verwerken en omzetten naar een bestand zoals `table.txt`.

## Klasse Team

Om te beginnen schrijven we een klasse `Team`. Bij het initialiseren van een `Team`-object willen we in staat zijn om de naam van het team mee te geven, zoals hieronder:

```
>>> liverpool = Team("Liverpool FC")
>>> liverpool.name
"Liverpool FC"
```

Daarnaast moet elk team de volgende informatie bijhouden:
- Hoeveel wedstrijden het heeft gespeeld.
- Hoeveel wedstrijden het heeft gewonnen, verloren en gelijkgespeeld.
- Hoeveel doelpunten het heeft gescoord in alle gespeelde wedstrijden.
- Hoeveel doelpunten het tegen heeft gekregen (aantal doelpunten gescoord door andere teams tegen dit team).
- Het doelsaldo (= gescoorde doelpunten - tegendoelpunten).
- Het aantal punten dat is verzameld in alle gespeelde wedstrijden (een team krijgt 3 punten voor een overwinning, 1 punt voor een gelijkspel en 0 punten voor een verlies).

Aanvankelijk worden al deze attributen op 0 gezet.

```
>>> liverpool.get_games_played()
0
>>> liverpool.games_won
0
>>> liverpool.games_lost
0
>>> liverpool.games_drawn
0
>>> liverpool.goals_scored
0
>>> liverpool.goals_conceded
0
>>> liverpool.get_goal_difference()
0
>>> liverpool.get_points()
0
```

### Een wedstrijd spelen
Nu willen we teams tegen elkaar laten spelen. Hiervoor definiëren we een methode `play` in `Team`, die een ander team als argument accepteert, evenals de doelpunten die beide teams hebben gescoord:

```
>>> barcelona = Team("FC Barcelona")
>>> liverpool.play(barcelona, 4, 1)
```

In dit geval is 4 het aantal doelpunten gescoord door Liverpool, en 1 het aantal doelpunten gescoord door Barcelona.

Het uitvoeren van deze methode moet de statistieken van beide betrokken teams bijwerken:

```
>>> liverpool.get_games_played()
1
>>> liverpool.games_won
1
>>> liverpool.goals_scored
4
>>> liverpool.goals_conceded
1
>>> liverpool.get_points()
3

>>> barcelona.get_games_played()
1
>>> barcelona.games_lost
1
>>> barcelona.goals_scored
1
>>> barcelona.goals_conceded
4
>>> barcelona.get_points()
0
```

Bij een volgende wedstrijd worden de nieuwe gegevens bij de bestaande statistieken opgeteld.

Bijvoorbeeld, als Liverpool opnieuw speelt tegen een nieuw team genaamd "AS Roma":
```
>>> roma = Team("AS Roma")
>>> liverpool.play(roma, 2, 2)
```
Dan zien we dat Liverpool's statistieken worden bijgewerkt op basis van de twee gespeelde wedstrijden (de vorige tegen Barcelona en deze tegen AS Roma).

Liverpool heeft nu twee wedstrijden gespeeld:
```
>>> liverpool.get_games_played()
2
```

Het heeft 4 punten: 3 van de wedstrijd tegen Barcelona (overwinning) en 1 van de wedstrijd tegen Roma (gelijkspel):
```
>>> liverpool.get_points()
4
```

Het heeft in totaal zes doelpunten gescoord: 4 tegen Barcelona en 2 tegen Roma:
```
>>> liverpool.goals_scored
6
```

Alle andere statistieken worden op dezelfde manier bijgewerkt.

## Klasse Competition
Vervolgens willen we deze teams bijhouden in een competitie. Om dit te doen, maak je een klasse `Competition`. Wanneer je een object van deze klasse aanmaakt, hoef je geen argumenten mee te geven. We zullen er later nog zaken aan toevoegen.
```
>>> champions_league = Competition()
```

### Teams toevoegen en opvragen
Om ervoor te zorgen dat onze competitie iets nuttigs kan doen, moeten we teams kunnen toevoegen aan onze competitie. Definieer een methode `add_team` die een teamnaam als argument neemt en dit team toevoegt aan de competitie:
```
>>> champions_league.add_team("Liverpool FC")
```
Om het resultaat hiervan te kunnen zien, moeten we ook een methode `get_team_by_name` definiëren die een teamnaam als argument neemt en het bijbehorende `Team` object teruggeeft:
```
>>> liverpool = champions_league.get_team_by_name("Liverpool FC")
>>> liverpool.name
"Liverpool FC"
>>> liverpool.get_games_played()
0
```
Zoals je ziet, wordt er een nieuw `Team` object aangemaakt wanneer een team aan de competitie wordt toegevoegd. Dit object vertegenwoordigt het team in die specifieke competitie.

### Westrijdinformatie verwerken
Definieer een methode `update_competition` die toelaat om de informatie van de teams in een competitie bij te werken aan de hand van een lijst met wedstrijdresultaten. Eén wedstrijdresultaat bestaat uit een tuple van de vorm `(team_a, team_b, score_a, score_b)`.
```
>>> champions_league.update_competition(
    [("Liverpool FC", "Real Madrid", 4, 1),
     ("AS Roma", "FC Barcelona", 1, 1),
     ("Liverpool FC", "AS Roma", 3, 1),
     ("Real Madrid", "FC Barcelona", 0, 2)]
)
>>> liverpool = champions_league.get_team_by_name("Liverpool FC")
>>> liverpool.get_points()
6
>>> liverpool.goals_scored
7
>>> liverpool.get_goal_difference()
5
>>> barcelona = champions_league.get_team_by_name("FC Barcelona")
>>> barcelona.get_points()
4
>>> barcelona.get_goal_difference()
2
```
Op dezelfde manier zullen alle andere statistieken worden bijgewerkt.

Merk op dat het mogelijk is dat de competitie één van de teams (of beide) die in het wedstrijdresultaat vermeld worden, nog niet bevat. In dat geval moet het team eerst aan de competitie worden toegevoegd.

### Competitie weergeven
Nu er enkele wedstrijden gespeeld zijn in onze competitie, willen we een mooi overzicht van hoe de verschillende teams ervoor staan.

Definieer een methode `display_table` die een string teruggeeft die de competitie-stand weergeeft als volgt:
```
>>> print(champions_league.display_table())
Team          | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts
Liverpool FC  | 2   | 2   | 0   | 0   | 7    | 2    | 5    | 6
Real Madrid   | 2   | 0   | 0   | 2   | 1    | 6    | -5   | 0
AS Roma       | 2   | 0   | 1   | 1   | 2    | 4    | -2   | 1
FC Barcelona  | 2   | 1   | 1   | 0   | 3    | 1    | 2    | 4
```

> Opmerking: Zoals je kunt zien, is deze tabel niet echt een ranglijst, omdat de teams niet in volgorde van hun prestaties worden weergegeven. Bijvoorbeeld, Barcelona heeft 4 punten, maar verschijnt toch als laatste in de tabel. Voor deze opdracht is het niet vereist dat `display_table` de teams sorteert op basis van hun prestaties. Voor degenen die hun teams wél in de juiste volgorde willen rangschikken, leggen we in het optionele gedeelte "De competitiestand sorteren" aan het einde van deze opdracht uit hoe je dit kunt doen.

## Wedstrijdinformatie inlezen
Laten we nu bekijken hoe we wedstrijdgegevens uit bestanden kunnen lezen.

### Bestandsformaat
In deze map zijn er twee bestanden met wedstrijdgegevens: `match_data_sample.txt`, dat slechts enkele wedstrijdresultaten bevat (voor testdoeleinden), en `match_data.txt`, dat heel veel wedstrijden bevat (simuleert een volledige competitie). In beide bestanden stelt elke regel één wedstrijd voor in het volgende formaat:
```
team_a - team_b: score_a - score_b
```
(raadpleeg één van de bestanden om het formaat beter te begrijpen)

### Een matchdata-bestand inlezen
Laten we eerst een functie `read_match_data_file` schrijven die zo een bestand kan lezen en een lijst teruggeeft met de wedstrijdresultaten die dat bestand bevat. De functie moet een lijst van tuples teruggeven, waarbij elke tuple het volgende formaat heeft: `(team_a, team_b, score_a, score_b)`
```
>>> read_match_data_file('match_data_sample.txt')
[('FC Liverpool', 'AS Roma', 2, 2),
 ('Man United', 'AC Milan', 3, 1),
 ('Bayern Munich', 'PSG', 0, 0)]
```

## Wegschrijven van de competitiestand
De volgende stap is onze competitieberekeningen op te slaan. Definieer hiervoor een methode `write_table` in de `Competition`-klasse die de competitiestand wegschrijft naar een opgegeven bestand:
```
>>> champions_league.write_table("champions_league_table.txt")
```
wat resulteert in een bestand `champions_league_table.txt` met de volgende inhoud:
```
Team          | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts
Liverpool FC  | 2   | 2   | 0   | 0   | 7    | 2    | 5    | 6
Real Madrid   | 2   | 0   | 0   | 2   | 1    | 6    | -5   | 0
AS Roma       | 2   | 0   | 1   | 1   | 2    | 4    | -2   | 1
FC Barcelona  | 2   | 1   | 1   | 0   | 3    | 1    | 2    | 4
```
(Merk op dat de inhoud van dit bestand hetzelfde is als de output van `display_table`)

## Het allemaal samenbrengen
Schrijf ten slotte de functie `process_match_data` die gebruikmaakt van alle eerder gedefinieerde klassen en functies. Deze functie neemt twee argumenten:

`match_data_file_name`: de naam van het bestand waaruit wedstrijdgegevens gelezen moeten worden
`output_file_name`: de naam van het bestand waarin de resulterende competitiestand moet worden weggeschreven
```
>>> process_match_data('match_data.txt', 'output.txt')
```
zou moeten resulteren in een bestand output.txt dat dezelfde inhoud heeft als table.txt, namelijk:
```
Team               | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts
RSC Anderlecht     | 15  | 15  | 0   | 0   | 39   | 17   | 22   | 45
Club Brugge        | 15  | 4   | 3   | 8   | 21   | 31   | -10  | 15
Real Madrid        | 15  | 10  | 3   | 2   | 30   | 16   | 14   | 33
FC Barcelona       | 15  | 9   | 2   | 4   | 32   | 23   | 9    | 29
Atletico Madrid    | 15  | 3   | 3   | 9   | 14   | 22   | -8   | 12
Arsenal            | 15  | 5   | 2   | 8   | 15   | 22   | -7   | 17
Liverpool          | 15  | 8   | 3   | 4   | 27   | 20   | 7    | 27
Man City           | 15  | 5   | 4   | 6   | 22   | 23   | -1   | 19
Man United         | 15  | 9   | 3   | 3   | 23   | 11   | 12   | 30
Chelsea FC         | 15  | 3   | 4   | 8   | 16   | 23   | -7   | 13
PSV                | 15  | 1   | 0   | 14  | 12   | 32   | -20  | 3
Ajax               | 15  | 8   | 3   | 4   | 31   | 22   | 9    | 27
PSG                | 15  | 6   | 4   | 5   | 28   | 27   | 1    | 22
Marseille          | 15  | 1   | 7   | 7   | 17   | 30   | -13  | 10
FC Bayern Munchen  | 15  | 7   | 5   | 3   | 26   | 20   | 6    | 26
Dortmund           | 15  | 0   | 6   | 9   | 12   | 26   | -14  | 6
```

## (Optioneel) De competitiestand sorteren
> Opmerking: Deze sectie is volledig optioneel. Er zullen geen vragen over gesteld worden op het examen en je wordt ook niet verwacht enige code die hier vermeld wordt te begrijpen.

Zoals eerder vermeld, is de resulterende tabel niet echt een competitiestand, omdat de tabel niet gesorteerd is op basis van de resultaten van de verschillende teams. We vereisen niet dat `display_table` de teams sorteert op prestaties, omdat we nog geen eenvoudige manier geleerd hebben om lijsten van objecten te sorteren op specifieke criteria. Als je de tabel toch wilt sorteren, kun je deze methode toevoegen aan je `Team`-klasse:
```python
def __lt__(self, other):
    """
    Compare two `Team` objects on points, games won, goal difference, goals
    scored and finally name.
    """
    if self.get_points() != other.get_points():
        return self.get_points() > other.get_points()

    if self.games_won != other.games_won:
        return self.games_won > other.games_won

    if self.get_goal_difference() != other.get_goal_difference():
        return self.get_goal_difference() > other.get_goal_difference()

    if self.goals_scored != other.goals_scored:
        return self.goals_scored > other.goals_scored

    return self.name < other.name
```
Je kunt vervolgens een gesorteerde lijst van teams verkrijgen door de ingebouwde functie `sorted` te gebruiken op een verzameling van `Team`-objecten. Hier is een voorbeeld van hoe `sorted` werkt op een lijst met getallen:
```
>>> unsorted_list = [3, 1, 6, 3, 8]
>>> sorted(unsorted_list)
[1, 3, 3, 6, 8]
```
Wanneer je deze `sorted` functie op de juiste plaats in je code gebruikt (waar het een verzameling van `Team`-objecten als argument neemt) en je de hierboven gespecificeerde `__lt__` functie aan de klasse `Team` hebt toegevoegd, krijg je dit resultaat (wat de inhoud is van `ranking.txt`):
```
>>> print(champions_league.display_table())
Team               | Pld | Won | Tie | Lst | Gls+ | Gls- | Diff | Pts
RSC Anderlecht     | 15  | 15  | 0   | 0   | 39   | 17   | 22   | 45
Real Madrid        | 15  | 10  | 3   | 2   | 30   | 16   | 14   | 33
Man United         | 15  | 9   | 3   | 3   | 23   | 11   | 12   | 30
FC Barcelona       | 15  | 9   | 2   | 4   | 32   | 23   | 9    | 29
Ajax               | 15  | 8   | 3   | 4   | 31   | 22   | 9    | 27
Liverpool          | 15  | 8   | 3   | 4   | 27   | 20   | 7    | 27
FC Bayern Munchen  | 15  | 7   | 5   | 3   | 26   | 20   | 6    | 26
PSG                | 15  | 6   | 4   | 5   | 28   | 27   | 1    | 22
Man City           | 15  | 5   | 4   | 6   | 22   | 23   | -1   | 19
Arsenal            | 15  | 5   | 2   | 8   | 15   | 22   | -7   | 17
Club Brugge        | 15  | 4   | 3   | 8   | 21   | 31   | -10  | 15
Chelsea FC         | 15  | 3   | 4   | 8   | 16   | 23   | -7   | 13
Atletico Madrid    | 15  | 3   | 3   | 9   | 14   | 22   | -8   | 12
Marseille          | 15  | 1   | 7   | 7   | 17   | 30   | -13  | 10
Dortmund           | 15  | 0   | 6   | 9   | 12   | 26   | -14  | 6
PSV                | 15  | 1   | 0   | 14  | 12   | 32   | -20  | 3
```
Als het je niet lukt om dit te laten werken, maak je geen zorgen. Dit is slechts een extraatje voor degenen die willen dat de tabel in de juiste volgorde wordt weergegeven. We zullen hier geen vragen over stellen op het examen.
