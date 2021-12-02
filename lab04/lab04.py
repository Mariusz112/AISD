from typing import Any, List


class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, value: Any):
        self.values.insert(0, value)

    def dequeue(self):
        return self.values.pop(len(self.values) - 1)

    def peek(self):
        return self.values[-1]

    def __len__(self):
        c = 0
        for x in self.values:
            c += 1
        return c

    def __str__(self):
        str = ""
        for x in self.values:
            str = str + ", "
        return str


class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.parent = None
        self.children = []

    def __str__(self):
        return self.value

    def level_of(self):
        lvl = 0
        parent = self.parent
        while parent != None:
            lvl += 1
            parent = parent.parent
        return lvl

    # is_leaf() -> bool, która sprawdzi czy węzeł jest liściem
    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    # add(child: 'TreeNode') -> None, która doda węzeł przyjęty w argumencie jako dziecko
    def add(self, child: 'TreeNode'):
        self.children.append(child)
        child.parent = self

    # for_each_deep_first(visit: Callable[['TreeNode'], None]) -> None, która wykona operację przechodzenia po węzłach
    # metodą deep first według następujących instrukcji: odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit (
    # przyjętą w parametrze) dla wszystkich dzieci bieżącego węzła wykonaj metodę for_each_deep_first()
    def for_each_deep_first(self):
        for c in self.children:
            type(self).for_each_deep_first(c)

    # for_each_level_order(visit: Callable[['TreeNode'], None]) -> None, która wykona operację przechodzenia po węzłach
    # metodą level order według następujących instrukcji: odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit
    # (przyjętą w parametrze) wszystkie dzieci bieżącego węzła dodaj do pustej kolejki FIFO dopóki kolejka nie jest
    # pusta, dla każdego pierwszego elementu w kolejce (element) odwiedź element dodaj do kolejki wszystkie węzły,
    # których rodzicem jest element
    def for_each_level_order(self):
        q = Queue()
        for c in self.children:
            q.enqueue(c)

        while len(q) != 0:
            t = q.peek()
            q.dequeue().value
            for c in t.children:
                q.enqueue(c)

    # search(value: Any) -> Union['TreeNode', None], która sprawdzi czy bieżący węzeł lub jego dzieci zawierają wartość
    # podaną w parametrze, przy użyciu dowolnej metody przechodzenia po węzłach
    def search(self, value: Any):
        if self.value == value:
            return self
        else:
            q = Queue()
            for c in self.children:
                q.enqueue(c)

            while len(q) != 0:
                t = q.peek()
                comp = q.dequeue()
                if comp.value == value:
                    return comp
                for c in t.children:
                    q.enqueue(c)
            return None


# Klasa Tree jest odpowiedzialna za przechowywanie całej struktury drzewa, gdzie root wskazuje węzeł będący korzeniem.
class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    # metoda add(value: Any, parent_name: Any) -> None doda nowe dziecko z wartością przekazaną w parametrze value,
    # którego rodzicem będzie węzeł przekazany w parametrze parent_value
    def add(self, value: Any, parent: Any):
        parent.children.append(TreeNode(value))

    # metoda for_each_level_order(visit: Callable[['TreeNode'], None]) -> None wykona operację przechodzenia po węzłach
    # metodą level order, rozpoczynając od korzenia
    def for_each_level_order(self):
        if type(self) is Tree:
            for c in self.root.children:
                print(c)
                Tree.for_each_level_order(c)
        if type(self) is TreeNode:
            for c in self.children:
                print(c)
                Tree.for_each_level_order(c)

    # metoda for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None wykona operację przechodzenia po
    # węzłach metodą deep first, rozpoczynając od korzenia
    def for_each_deep_first(self):
        r = self.root
        q = Queue()
        for c in r.children:
            q.enqueue(c)

        while len(q) != 0:
            t = q.peek()
            q.dequeue()
            for c in t.children:
                q.enqueue(c)

    # metoda show wyświetli drzewo w formie graficznej, można użyć w tym celu bibliotek zewnętrznych
    def show(self):
        root = "-"

        if type(self) is Tree:
            print(self.root.value)
            for c in self.root.children:
                print(root * c.level_of() + c.value)
                Tree.show(c)
        if type(self) is TreeNode:
            for c in self.children:
                print(root * c.level_of() + c.value)
                Tree.show(c)


tF = TreeNode("F")
tB = TreeNode("B")  # 2
tG = TreeNode("G")  # 2
tA = TreeNode("A")  # 3-B
tD = TreeNode("D")  # 3-B
tI = TreeNode("I")  # 3-Q
tC = TreeNode("C")  # 4-D
tE = TreeNode("E")  # 4-D
tH = TreeNode("H")  # t-I
tree = Tree(tF)
tF.add(tB)
tF.add(tG)
tB.add(tA)
tB.add(tD)
tG.add(tI)
tD.add(tC)
tD.add(tE)
tI.add(tH)
tree.show()
