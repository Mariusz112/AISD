# zad2 Mariusz Raś
# do przechowywania wartości wewnątrz stosu wykorzystać własną implementację klasy LinkedList
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


# klasa Stack będzie reprezentacją stosu
class Stack:

    # wywołanie inicjalizatora klasy Stack utworzy pusty stos
    def __init__(self):
        self.head = None

    # sprawdz czy stos jest pusty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    # metoda push(self, element: Any) -> None umieści nową wartość "na szczycie" stosu, czyli zostanie dodana na końcu wewnętrznej listy
    def push(self, data):

        if self.head == None:
            self.head = LinkedList(data)

        else:
            newnode = LinkedList(data)
            newnode.next = self.head
            self.head = newnode

    # metoda pop(self) -> Any zwróci i usunie wartość ze szczytu stosu
    def pop(self):

        if self.isempty():
            return None

        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    # Returns the head LinkedList data
    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    # print
    def print(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, "\n", end="")
                iternode = iternode.next
            return

    # dlugosc stosu
    def len(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count


# Driver code
stack = Stack()

stack.push(3)
stack.push(10)
stack.push(1)
stack.push(0)

# print stack elements
stack.print()

# Print top element of stack
print("\nTop element is ", stack.peek())
stack.pop()

# print stack elements
stack.print()
print("\nTop element is ", stack.peek())
print("\n")
stack.print()

print("\nLiczba elementów stosu to :", stack.len())