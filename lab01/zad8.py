# zad 7
lst = []
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
    print(lst)


def convert(lst):
    return tuple(lst)


print(convert(lst))