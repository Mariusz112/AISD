from enum import Enum
from typing import Any
from typing import Dict, List
from typing import Optional
from queue import Queue as test
from graphviz import Digraph as Groph


# Mariusz Raś - projekt 3
# Niech g będzie grafem nieważonym skierowanym (obiektem klasy Graph z lab 7) wypełnionym dowolnymi wierzchołkami.
# Przygotować funkcję paths_count(g: Graph, a: Any, b: Any) -> int, która zwróci liczbę wszystkich ścieżek pomiędzy
#  wierzchołkami a i b (zawierającymi wartości przekazane w argumentach a i b).
#
# Celem sprawdzenia rozwiązania przygotować 3 dowolne grafy testowe.

# Klasa przechowująca węzły grafu:
# gdzie data oznacza wartość przechowywaną w grafie, a index będzie numerem pozycji na liście sąsiedztwa.
class Vertex:
    data: Any
    index: int

    def __init__(self, data, ind):
        self.data = data
        self.index = ind

    def __repr__(self):
        return f'{self.data}:v{self.index}'


# Klasa przechowująca krawędzie grafu:
# gdzie wartość wagi krawędzi jest opcjonalna (może posiadać wartość None).
class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, s, d, w):
        self.source = s
        self.destination = d
        self.weight = w

    def __repr__(self):
        return f'{self.destination}'


# Klasa enumeratora zawierającego typy krawędzi
class EdgeType(Enum):
    directed = 1
    undirected = 2


# Klasa przechowująca strukturę grafu:
class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()

    def __repr__(self):
        stirng = ""
        for data in self.adjacencies:
            stirng += f'- {data} ->{self.adjacencies[data]}\n'
        return stirng

    # create_vertex(self, data: Any) -> Vertex, która doda nowy wierzchołek do słownika adjacencies jako klucz i
    # pustą listę sąsiedztwa jako wartość
    def create_vertex(self, data: Any):
        self.adjacencies[Vertex(data, len(self.adjacencies))] = list()

    # add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None,
    # która doda nową krawędź od wierzchołka source do wierzchołka destination i umieści ją w słowniku adjacencies
    # w liście sąsiedztwa wierzchołka początkowego tej krawędzi
    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))

    # add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None,
    # która stworzy krawędź skierowaną od source do destination i na odwrót
    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source, destination, weight))
        self.adjacencies[destination].append(Edge(destination, source, weight))

    # add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None,
    # która w zależności od typu krawędzi w parametrze edge, doda nową krawędź w grafie
    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    # traverse_breadth_first(self, visit: Callable[[Any], None]) -> None, która wykona operację przechodzenia wszerz po
    # grafie skierowanym. Wykorzystać własną implementację klasy Queue (kolejka, lab 2, zadanie 3)
    def traverse_breadth_first(self, visit):
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        queue = test.Queue()
        queue.enqueue(list_keys[0])
        while (len(queue) != 0):
            new = queue.dequeue()
            list_visited.append(new)
            visit(new)
            for new_neighbour in self.adjacencies[new]:
                if new_neighbour.destination in list_visited:
                    True
                else:
                    queue.enqueue(new_neighbour.destination)

    # traverse_depth_first(self, visit: Callable[[Any], None]) -> None, która wykona operację przechodzenia
    # w głąb po grafie skierowanym
    def traverse_depth_first(self, visit):
        list_keys = [x for x in self.adjacencies.keys()]
        list_visited = []
        self._dfs(list_keys[0], list_visited, visit)

    # Odwiedzanie rozpoczynamy od wierzchołka początkowego. Następnie przechodzimy do sąsiadów wierzchołka
    # początkowego i je również oznaczamy jako odwiedzone. Operację kończymy gdy zostaną odwiedzone tym
    # sposobem wszystkie wierzchołki.
    def _dfs(self, v: Vertex, visited: List[Vertex], visit):
        visit(v)
        visited.append(v)
        for new_neighbour in self.adjacencies[v]:
            if new_neighbour.destination in visited:
                True
            else:
                self._dfs(new_neighbour.destination, visited, visit)

    # metoda show(), która wyświetli graf wraz ze skierowanymi lub nieskierowanymi krawędziami i ich wagami
    def show(self, name="graph"):
        dot = Groph()
        visited = []
        for x in self.adjacencies.keys():
            self._show_helper(x, dot, visited)
        dot.render(f'paths_count/{name}', view=True, format="png", quiet_view=False)

    # Show helper tworzy wierzcholki dla siebie i sasiadow
    def _show_helper(self, v: Vertex, dot, visited: List):
        if v in visited:
            True
        else:
            dot.node(str(v.index), str(v.data))
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                desc = ""
                if neighbour.weight != None:
                    desc += f"{neighbour.weight}"
                dot.edge(str(neighbour.source.index), str(neighbour.destination.index), label=desc)
                if not (neighbour.destination in visited):
                    self._show_helper(neighbour.destination, dot, visited)


# Dfs przeszukuje kazdy poziom jak znajdzie to zwraca wynik
# Adjacencies to slownik kluczy
# vertex to petla z warunkiem wierzcholka wykorzystujac iterator czyli
# przechowanie obiektu a next to funkcja sprawdzajaca to co ma w sobie po grafie
def paths_count(g: Graph, a: Any, b: Any) -> int:
    vertices = g.adjacencies.keys()

    a_vertex = next(iter([v for v in vertices if v.data == a]))
    b_vertex = next(iter([v for v in vertices if v.data == b]))

    return dfs_count(g, a_vertex, b_vertex, [0])


# Petla szukajaca krawedzi ze slownika kluczy jesli konczy sie na sasiedzie  to wyswietl znaleziono i zwraca sciezke
def dfs_count(g: Graph, start: Vertex, end: Vertex, countRef, visited=set()) -> int:
    own_visited = set(visited)
    own_visited.add(start)

    for edge in g.adjacencies[start]:
        neigbour = edge.destination

        if neigbour == end:
            countRef[0] += 1
            # print('Found:')
            # print(own_visited)
            continue

        if neigbour not in visited:
            dfs_count(g, neigbour, end, countRef, own_visited)

    return countRef[0]


# def zad():
#     graph = Graph()
#     names = [
#         'Ala',
#         'Roman',
#         'Adam',
#         'Ola',
#         'Michal',
#         'Rafal',
#         'Kuba',
#         'Lukasz'
#     ]
#
#     for n in names:
#         graph.create_vertex(n)
#
#     graph_keys = graph.adjacencies.keys()
#     vertices = dict(zip(names, graph_keys))
#
#     graph.add(EdgeType.directed, vertices['Ala'], vertices['Roman'])
#     graph.add(EdgeType.directed, vertices['Ala'], vertices['Adam'])
#     graph.add(EdgeType.directed, vertices['Michal'], vertices['Rafal'])
#     graph.add(EdgeType.directed, vertices['Adam'], vertices['Rafal'])
#     graph.add(EdgeType.directed, vertices['Lukasz'], vertices['Roman'])
#     graph.add(EdgeType.directed, vertices['Ola'], vertices['Ala'])
#     graph.add(EdgeType.directed, vertices['Kuba'], vertices['Ala'])
#     graph.add(EdgeType.directed, vertices['Kuba'], vertices['Michal'])
#     graph.add(EdgeType.directed, vertices['Adam'], vertices['Lukasz'])
#     graph.add(EdgeType.directed, vertices['Roman'], vertices['Rafal'])
#     graph.add(EdgeType.directed, vertices['Michal'], vertices['Lukasz'])
#
#     amount = paths_count(graph, 'Ala', 'Lukasz')
#     print(f'Paths count: {amount} (Ala -> Lukasz)')
#
#     amount = paths_count(graph, 'Ola', 'Roman')
#     print(f'Paths count: {amount} (Ola -> Roman)')
#
#     amount = paths_count(graph, 'Kuba', 'Rafal')
#     print(f'Paths count: {amount} (Kuba -> Rafal)')
#
#     graph.show(name="zad")


def test1():
    graph = Graph()
    names = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['A'], vertices['B'])
    graph.add(EdgeType.directed, vertices['A'], vertices['C'])
    graph.add(EdgeType.directed, vertices['C'], vertices['B'])
    graph.add(EdgeType.directed, vertices['C'], vertices['E'])
    graph.add(EdgeType.directed, vertices['D'], vertices['F'])
    graph.add(EdgeType.directed, vertices['F'], vertices['A'])
    graph.add(EdgeType.directed, vertices['H'], vertices['B'])
    graph.add(EdgeType.directed, vertices['H'], vertices['G'])
    graph.add(EdgeType.directed, vertices['G'], vertices['E'])
    graph.add(EdgeType.directed, vertices['G'], vertices['D'])
    graph.add(EdgeType.directed, vertices['B'], vertices['E'])
    graph.add(EdgeType.directed, vertices['D'], vertices['A'])

    amount = paths_count(graph, 'H', 'E')
    print(f'Paths count: {amount} (H -> E)')

    graph.show(name="test1")


def test2():
    graph = Graph()
    names = [
        'Ala',
        'Adam',
        'Julia',
        'Zofia',
        'Hanna',
        'Franciszek ',
        'Jan',
        'Jakub',
        'Szymon',
        'Filip',
        'Laura',
        'Maria'
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['Ala'], vertices['Adam'])
    graph.add(EdgeType.directed, vertices['Ala'], vertices['Julia'])
    graph.add(EdgeType.directed, vertices['Zofia'], vertices['Ala'])
    graph.add(EdgeType.directed, vertices['Hanna'], vertices['Zofia'])
    graph.add(EdgeType.directed, vertices['Hanna'], vertices['Franciszek '])
    graph.add(EdgeType.directed, vertices['Franciszek '], vertices['Szymon'])
    graph.add(EdgeType.directed, vertices['Filip'], vertices['Laura'])
    graph.add(EdgeType.directed, vertices['Maria'], vertices['Szymon'])
    graph.add(EdgeType.directed, vertices['Jan'], vertices['Ala'])
    graph.add(EdgeType.directed, vertices['Szymon'], vertices['Jakub'])
    graph.add(EdgeType.directed, vertices['Filip'], vertices['Maria'])
    graph.add(EdgeType.directed, vertices['Jan'], vertices['Hanna'])
    graph.add(EdgeType.directed, vertices['Laura'], vertices['Jan'])
    graph.add(EdgeType.directed, vertices['Julia'], vertices['Laura'])
    graph.add(EdgeType.directed, vertices['Szymon'], vertices['Jan'])
    graph.add(EdgeType.directed, vertices['Laura'], vertices['Maria'])

    amount = paths_count(graph, 'Laura', 'Julia')
    print(f'Paths count: {amount} (Laura -> Julia)')

    amount = paths_count(graph, 'Szymon', 'Franciszek ')
    print(f'Paths count: {amount} (Szymon -> Franciszek )')

    graph.show(name="test2")


def test3():
    graph = Graph()
    names = [
        'Facebook',
        'Google',
        'Youtube',
        'Whatsapp',
        'Instagram',
        'Snapchat',
        'Discord'
    ]

    for n in names:
        graph.create_vertex(n)

    graph_keys = graph.adjacencies.keys()
    vertices = dict(zip(names, graph_keys))

    graph.add(EdgeType.directed, vertices['Facebook'], vertices['Google'])
    graph.add(EdgeType.directed, vertices['Facebook'], vertices['Youtube'])
    graph.add(EdgeType.directed, vertices['Google'], vertices['Whatsapp'])
    graph.add(EdgeType.directed, vertices['Google'], vertices['Snapchat'])
    graph.add(EdgeType.directed, vertices['Instagram'], vertices['Google'])
    graph.add(EdgeType.directed, vertices['Youtube'], vertices['Instagram'])
    graph.add(EdgeType.directed, vertices['Snapchat'], vertices['Facebook'])
    graph.add(EdgeType.directed, vertices['Snapchat'], vertices['Discord'])
    graph.add(EdgeType.directed, vertices['Discord'], vertices['Youtube'])
    graph.add(EdgeType.directed, vertices['Whatsapp'], vertices['Discord'])
    graph.add(EdgeType.directed, vertices['Whatsapp'], vertices['Instagram'])

    amount = paths_count(graph, 'Facebook', 'Discord')
    print(f'Paths count: {amount} (Facebook -> Discord)')

    amount = paths_count(graph, 'Youtube', 'Google')
    print(f'Paths count: {amount} (Youtube -> Google)')

    amount = paths_count(graph, 'Whatsapp', 'Youtube')
    print(f'Paths count: {amount} (Whatsapp -> Youtube)')

    graph.show(name="test3")


# print("Lab7")
# zad()

print("\nTest1")
test1()

print("\ntest2")
test2()

print("\ntest3")
test3()
