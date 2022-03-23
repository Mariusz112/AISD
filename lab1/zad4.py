print("Program zastosuje funkcje do podanych danych, podaj ktorego programu chcesz  uzyc (1 lub 2)")
def zad4():
    print("")
case = input()
match case:
    case "1":
        print("Podaj Imie")
        x = input()
        print("Podaj Nazwisko")
        y = input()
        first_char = x[0]
        print(first_char, ".", y)
    case "2":
        print("Podaj Imie")
        x = input()
        print("Podaj Nazwisko")
        y = input()
        first_char = x[0]
        print(first_char.capitalize(), ".", y.capitalize())

    case _:
        print("Nie ma programu o takim numerze")


zad4()