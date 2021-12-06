# Mariusz Raś
from typing import Any


class BinaryTree:
    def __init__(self,  value: Any, null=None):
        self.value = value
        self.left_child: BinaryTree = null
        self.right_child: BinaryTree = null
        self.parent: BinaryTree = null

    # add_left_child(self, value: Any), która doda lewe dziecko bieżącego węzła jako nowy węzeł
    def add_left_child(self, value: Any):
        self.left_child = BinaryTree(value)
        self.left_child.parent = self

    # add_right_child(self, value: Any), która doda prawe dziecko bieżącego węzła jako nowy węzeł
    def add_right_child(self, value: Any):
        self.right_child = BinaryTree(value)
        self.right_child.parent = self


# Recursive function to print the left view of a given binary tree
def left_line(tree, level=1, last_level=0):
    # base case: empty tree
    if tree is None:
        return last_level

    # if the current node is the first node of the current level
    if last_level < level:
        # print the node's data
        print(tree.value, end=' ')

        # update the last level to the current level
        last_level = level

    # recur for the left and right subtree by increasing the level by 1
    last_level = left_line(tree.left_child, level + 1, last_level)
    last_level = left_line(tree.right_child, level + 1, last_level)

    return last_level


tree = BinaryTree(1)

tree.add_left_child(2)
tree.add_right_child(3)

tree.left_child.add_left_child(4)
tree.left_child.add_right_child(5)

tree.right_child.add_right_child(7)

tree.left_child.left_child.add_left_child(8)
tree.left_child.right_child.add_right_child(9)

# Recursive implementation using Preorder traversal
# Przygotować funkcję left_line(tree: print) -> List[BinaryTree], która przyjmie argument
# tree w postaci drzewa binarnego (zaimplementowanego samodzielnie przy pomocy Lab 5) i
# zwróci listę węzłów tego drzewa, które stanowią jego lewostronną warstwę widokową:
# Dla przykładowego drzewa (powyżej) funkcja zwróci węzły o następujących wartościach: 1, 2,
# 4, 8
left_line(tree)