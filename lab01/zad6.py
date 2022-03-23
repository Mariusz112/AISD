def zad6():
    '''Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli, dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.'''
    print("bedziesz podawal liczby az ich suma przekroczy 100")


    a = int(input('Enter a number (-1 to quit): '))
    c = 0
    while c < 100:


        b = a
        c = b + a
        if c > 99:
            print("Suma liczb wynois =>", c)
            break
zad6()