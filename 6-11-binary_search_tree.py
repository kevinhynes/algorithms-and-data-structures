class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print(f'There is already a node with the value of {value}')

    def print_tree(self):
        if self.root == None:
            print(f'There is no root of this tree')
        else:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

def build_tree(bst, num_nodes=50, max_val=1000):
    from random import randint
    for num in range(num_nodes):
        new_node = randint(0, max_val)
        bst.insert(new_node)

tree = BST()
build_tree(tree)
tree.print_tree()