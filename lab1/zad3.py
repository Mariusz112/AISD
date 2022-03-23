def zad3():
    print("Podaj dwie pierwsze cyfry aktualnego roku")
    x = input()
    print("Podaj dwie ostatnie cyfry aktualnego roku")
    y = input()
    converted_num = str(x) + str(y)
    print("Podaj swój wiek")
    c = input()
    converted_num1 = float(converted_num)
    converted_num2 = float(c)
    print(type(converted_num1))

    rokurodzenia = converted_num1-converted_num2
    print(rokurodzenia)


zad3()
