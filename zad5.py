def zad5():
    '''Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia. Należy sprawdzić w jednej instrukcji if (bez użycia elif i else), czy obydwie liczby są dodatnie oraz czy druga liczba jest różna od 0.'''

    print("podaj 1 liczbe")
    a = input()
    print("podaj 2 liczbe")
    b = input()
    a1 = int(a)
    b1 = int(b)
    if(not (b1 != 0)):
        print("druga liczba jest równa zeru program nie zadziała poprawnie")
    z = 0
    if a1 > z:
        print("a > 0")
    if b1 > z:
        print("b > 0")

    c = a1/b1
    print("wynik z dzienia liczb")
    print(c)

zad5()