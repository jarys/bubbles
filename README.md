# Bubbles
World Editor ke hře Bubble Blast.

## Instalace

Naprogramováno pro python 3

Je potřeba nainstalovat knihovnu **pyglet** příkazem
```
pip install pyglet
```

Program lze spustit příkazem
```
python bubbles.py
```

## Ovládání

- myš
	- levé - umístit strukturu
	- střed - odpálit bublinu
	- pravé - smazat bublinu
	- kolečko - zoom

- WSAD - pohyb kamery

- F1 - vyčistit
- F2 - načíst soubor (potřeba zadat jméno do příkazové řádky)
- F5 - obnovit
- CTRL + S - uložit (při první uložení potřeba zadat jméno do příkazové řádky)

- QE - zpomalit / zrychlit

- 1234 - bubliny
- středník - nic

- CTRL + [klávesa] - uloží výtvor na klávesu

## Zevrubný přehled struktur

- J - and
- O - or
- N - neg
- X - xor
- Y - add

**set.txt** je přenos signálu v jedné dimenzi předvedený na semináři. Pro načtění stisknout F2 a napsat do terminálu *set.txt*

**double{and|or|neg|2}.txt** jsou strukctury pro signál 1/2

**comp{and|or|neg}.txt** jsou kompaktnější struktury pro signál 0/1








