# zad 10
'''Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków, a następnie zwróci wartość logiczną informującą o tym czy przekazany tekst jest palindromem.'''


def ispalindrome(str):

    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


# main function
s = input()
ans = ispalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")