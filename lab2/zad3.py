# zad3 Mariusz Raś
# do przechowywania wartości wewnątrz kolejki FIFO wykorzystać własną implementację listy (LinkedList)
class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None


# klasa Queue będzie reprezentacją kolejki FIFO
class Queue:
    # wywołanie inicjalizatora klasy Queue utworzy pustą kolejkę
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # metoda enqueue(self, element: Any) -> None umieści nowy element na końcu kolejki
    def EnQueue(self, item):
        temp = LinkedList(item)
    # metoda peek(self) -> Any zwróci wartość pierwszego elementu w kolejce
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # metoda dequeue(self) -> Any zwróci i usunie pierwszy element w kolejce
    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None
            return self.front

    # wywołanie funkcji len na obiekcie kolejki zwróci jej liczebność
    def len(self):
        temp = self.front  # Initialise temp
        count = 0  # Initialise count
        while temp:
            count += 1
            temp = temp.next
        return count

    # wywołanie funkcji print na obiekcie kolejki wypisze na ekranie jej elementy we właściwej kolejności
    def print(self):

        iternode = self.front
        if self.isEmpty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, "\n", end="")
                iternode = iternode.next
            return


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(15)
    q.EnQueue(25)
    q.EnQueue(30)
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.print()
    q.DeQueue()
    print("\n")
    q.print()
    print("\n")
    print("Queue Front " + str(q.front.data))
    print("\nLiczba elementów stosu to :", q.len())