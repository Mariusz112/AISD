'''Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy, a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu argumentowi. Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.'''
def zad8():
    thisdict = {
        "1": "pon",
        "2": "wto",
        "3": "sro",
        "4": "czw",
        "5": "pia",
        "6": "sob",
        "7": "nie",


    }
    print(thisdict)
    a = input()
    print(thisdict[a])
zad8()