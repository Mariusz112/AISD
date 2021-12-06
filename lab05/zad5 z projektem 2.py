from typing import Any

from collections import deque


class BinaryNode:
    def __init__(self,  value: Any, null=None):
        self.value = value
        self.left_child: BinaryNode = null
        self.right_child: BinaryNode = null
        self.parent: BinaryNode = null

    def __str__(self):
        return str(self.value)

    def level_of(self):
        lvl = 0
        parent = self.parent
        while parent is not None:
            lvl += 1
            parent = parent.parent

        return lvl

    # is_leaf(), która sprawdzi czy węzeł jest liściem
    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    # add_left_child(self, value: Any), która doda lewe dziecko bieżącego węzła jako nowy węzeł
    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)
        self.left_child.parent = self

    # add_right_child(self, value: Any), która doda prawe dziecko bieżącego węzła jako nowy węzeł
    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)
        self.right_child.parent = self

    # traverse_in_order(self, visit: Callable[[Any], None]), która wykona operację poprzecznego przejścia po
    # podrzędnych węzłach
    def traverse_in_order(self):

        if self.left_child:
            type(self).traverse_in_order(self.left_child)
        print(self.value)
        if self.right_child:
            type(self).traverse_in_order(self.right_child)

    # traverse_post_order(self, visit: Callable[[Any], None]), która wykona operację wstecznego przejscia po
    # podrzędnych węzłach
    def traverse_post_order(self):
        if self.left_child:
            type(self).traverse_post_order(self.left_child)
        if self.right_child:
            type(self).traverse_post_order(self.right_child)
        print(self.value)

    # traverse_pre_order(self, visit: Callable[[Any], None]), która wykona operację wzdłużnego przejścia po
    # podrzędnych węzłach
    def traverse_pre_order(self):
        print(self.value)
        if self.left_child:
            type(self).traverse_pre_order(self.left_child)
        if self.right_child:
            type(self).traverse_pre_order(self.right_child)


# Recursive function to print the left view of a given binary tree
def leftView(tree, level=1, last_level=0):
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
    last_level = leftView(tree.left_child, level + 1, last_level)
    last_level = leftView(tree.right_child, level + 1, last_level)

    return last_level


class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.value = None
        self.right_child = None
        self.left_child = None
        self.root = root

    # traverse_in_order(self, visit: Callable[[Any], None]), która wykona operację poprzecznego przejścia po
    # podrzędnych węzłach rozpoczynając od korzenia
    def traverse_in_order(self):
        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryNode.traverse_in_order(self.root.left_child)
            print(self.root.value)
            if self.root.right_child:
                BinaryNode.traverse_in_order(self.root.right_child)
        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.traverse_in_order(self.left_child)
            print(self.value)
            if self.right_child:
                BinaryTree.traverse_in_order(self.right_child)

    # traverse_post_order(self, visit: Callable[[Any], None]), która wykona operację wstecznego przejscia po
    # podrzędnych węzłach rozpoczynając od korzenia
    def traverse_post_order(self):
        if type(self) is BinaryTree:
            if self.root.left_child:
                BinaryNode.traverse_post_order(self.root.left_child)

            if self.root.right_child:
                BinaryNode.traverse_post_order(self.root.right_child)
            print(self.root.value)
        if type(self) is BinaryNode:
            if self.left_child:
                BinaryTree.traverse_post_order(self.left_child)

            if self.right_child:
                BinaryTree.traverse_post_order(self.right_child)
            print(self.value)

    # traverse_pre_order(self, visit: Callable[[Any], None]), która wykona operację wzdłużnego przejścia po
    # podrzędnych węzłach rozpoczynając od korzenia
    def traverse_pre_order(self):
        if type(self) is BinaryTree:
            print(self.root.value)
            if self.root.left_child:
                BinaryNode.traverse_pre_order(self.root.left_child)

            if self.root.right_child:
                BinaryNode.traverse_pre_order(self.root.right_child)

        if type(self) is BinaryNode:
            print(self.value)
            if self.left_child:
                BinaryNode.traverse_pre_order(self.left_child)

            if self.right_child:
                BinaryNode.traverse_pre_order(self.right_child)

    # metoda show wyświetli drzewo w formie grafting lub tekstowej, można użyć w tym celu bibliotek zewnętrznych
    def show(self):
        spacer = " |===|"
        if type(self) is BinaryTree:
            if self.root.right_child:
                BinaryTree.show(self.root.right_child)
            print("|" + str(self.root.value) + "|")
            if self.root.left_child:
                BinaryTree.show(self.root.left_child)
        if type(self) is BinaryNode:
            if self.right_child:
                BinaryTree.show(self.right_child)

            print("  " + spacer * self.level_of() + str(self.value) + "|")
            if self.left_child:
                BinaryTree.show(self.left_child)


tree = BinaryNode(10)


tree.add_left_child(9)
tree.add_right_child(2)

tree.left_child.add_left_child(1)
tree.left_child.add_right_child(3)

tree.right_child.add_left_child(4)
tree.right_child.add_right_child(6)

tree.left_child.left_child.add_left_child(9)
tree.left_child.right_child.add_right_child(8)

tree.right_child.left_child.add_right_child(2)
tree.right_child.right_child.add_left_child(5)
print("tree.traverse_in_order()")
tree.traverse_in_order()
print("tree.traverse_post_order()")
tree.traverse_post_order()
print("tree.traverse_pre_order()")
tree.traverse_pre_order()
bt = BinaryTree(tree)
print("drzewo")
bt.show()
# is leaf
print("tree.left_child.is_leaf()")
print(tree.left_child.is_leaf())
# Recursive implementation using Preorder traversal
leftView(tree)