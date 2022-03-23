# Zad1 Mariusz Raś

# klasa Node będzie reprezentacją węzła
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# klasa LinkedList będzie reprezentacją listy jednokierunkowej
class LinkedList:
    def __init__(self):
        self.head = None

    # metoda push(self, value: Any) -> None umieści nowy węzeł na początku listy
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # metoda append(self, value: Any) -> None umieści nowy węzeł na końcu listy
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printLista(self):
        temp = self.head
        while temp:
            print(' ' + str(temp.data), end=' -> ')
            temp = temp.next

    # metoda node(self, at: int) -> Node zwróci węzeł znajdujący się na wskazanej pozycji
    def node(self, index, false=None):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        assert false
        return 0

    # metoda remove_last(self) -> Any usunie ostatni element z listy i go zwróci
    def remove(self, position):
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    # funkcja len wywołana na obiekcie listy zwróci jej długość
    def len(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while temp:
            count += 1
            temp = temp.next
        return count


# metoda pop(self) -> Any usunie pierwszy element z listy i go zwróci
def pop(head):
    if not head:
        return None
    temp = head
    head = head.next
    temp = None
    return head


# metoda remove_last(self) -> Any usunie ostatni element z listy i go zwróci
def remove_last(head):
    if head is None:
        return None
    if head.next is None:
        head = None
        return None
    second_last = head
    while second_last.next.next:
        second_last = second_last.next
    second_last.next = None
    return second_last.data


def getNode(data):
    newnode = Node(data)
    return newnode


# metoda insert(self, value: Any, after: Node) -> None wstawi nowy węzeł tuż za węzłem wskazanym w parametrze
def insert(headnode, position, data):
    head = headnode
    if position < 1:
        print("Invalid position!")

    if position == 1:
        newnode = Node(data)
        newnode.next = headnode
        head = newnode

    else:
        while position != 0:
            position -= 1

            if position == 1:
                newnode = getNode(data)
                newnode.next = headnode.next
                headnode.next = newnode
                break

            headnode = headnode.next
            if headnode is None:
                break
        if position != 1:
            print("position out of range")
    return head


# funkcja print wywołana na obiekcie listy zawierającym 2 elementy [0, 1] wyświetli na ekranie "0 -> 1"
def printList(head):
    while head is not None:
        print(' ' + str(head.data), end=' -> ')
        head = head.next
    print()


# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.append(8)
    print('Lista jednokierunkowa to:', llist.printLista())
    n = 3
    print("Element o indeksie 3 to :", llist.node(n))
    head = getNode(1)
    head.next = getNode(7)
    head.next.next = getNode(6)
    head.next.next.next = getNode(4)
    print("Lista jednokierunkowa przez zmianą: ", end='')
    printList(head)
    data = 12
    position = 3
    head = insert(head, position + 1, data)
    print("Lista jednokierunkowa po umieszczeniu 12 po indeksie o numerze 2: \n", end='')
    printList(head)

    llist.printLista()
    llist.remove(1)
    print("\nLista jednokierunkowa po usunięciu elementu o indeksie 1: ")
    llist.printLista()
    print("\nLiczba węzłów listy jednokierunkowej to :", llist.len())




