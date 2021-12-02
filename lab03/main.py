n = int(input("Podaj n"))
text = str(input("Podaj tekst"))
def numbers(i):
    # warunek brzegowy - konczymy rekurencje gdy
    # wartosc parametru i spadnie ponizej zera
    if i < 0:
        return
    print(f' {i}')
    numbers(i - 1)



def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)



def power(num : int, n : int):
    if(n == 0):
        return 1
    else:

            return num * power(num, n-1)

def reverse(txt):
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

def factorial(n:int):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# driver code
numbers(n)
print(fib(n))
print(power(4, n))
print(reverse(text))
print(factorial(n))
# 6, 7, 8, 9, 10 brak