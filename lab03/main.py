n = int(input("Podaj n"))
text = str(input("Podaj tekst"))


# Zaimplementować funkcję numbers(n: int), która wypisze liczby od n do 0
def numbers(i):
    if i < 0:
        return
    print(f' {i}')
    numbers(i - 1)


# Zaimplementować funkcję fib(n: int) -> int, która obliczy n-ty wyraz ciągu Fibonacciego
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Zaimplementować funkcję power(number: int, n: int) -> int, której zadaniem jest zwrócenie wyniku działania $ number^n $ NIE UŻYWAĆ OPERATORA **
def power(num: int, n: int):
    if (n == 0):
        return 1
    else:

        return num * power(num, n - 1)


# Zaimplementować funkcję reverse(txt: str) -> str, która zwróci odwrócony ciąg znaków przekazany w parametrze txt
def reverse(txt):
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]


# Zaimplementować funkcję factorial(n: int) -> int, która zwróci silnię wartości przekazanej w parametrze
def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# driver code
numbers(n)
print(fib(n))
print(power(4, n))
print(reverse(text))
print(factorial(n))
# 6, 7, 8, 9, 10 brak
