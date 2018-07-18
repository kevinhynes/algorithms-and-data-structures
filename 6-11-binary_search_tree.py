class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def has_no_children(self):
        if self.left_child == None and self.right_child == None:
            return True

    def has_one_child(self):
        if self.left_child != None and self.right_child == None:
            return True
        elif self.left_child == None and self.right_child != None:
            return True
        else:
            return False

    def has_two_children(self):
        if self.left_child != None and self.right_child != None:
            return True
        else:
            return False

    def has_left_child(self):
        if self.left_child != None:
            return True
        else:
            return False
        
    def has_right_child(self):
        if self.right_child != None:
            return True
        else:
            return False

    def is_left_child(self):
        if self.parent.left_child == self:
            return True
        else:
            return False

    def is_right_child(self):
        if self.parent.right_child == self:
            return True
        else:
            return False
    

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        if self.root == None:
            return "There is no root to this tree."
        height = self.height
        leaf_nodes = 2**(height-1)      # Assume perfect binary tree to space nodes 
        width = (3*leaf_nodes*2) - 3    # 3 spaces per node & 3 spaces to separate nodes
        cur_height, cur_index = 0, 0
        tree_list = [['XXX' for j in range(2**i)] for i in range(height)]
        tree_list = self._repr(self.root, cur_height, cur_index, tree_list, height)
        tree_ascii = ''
        for i in range(len(tree_list)):
            row_as_string = ''
            for n in tree_list[i]:
                spacing = width//(len(tree_list[i])) + 1
                row_as_string += n.center(spacing, ' ')
            tree_ascii += row_as_string.center(width, ' ') + '\n'
        return tree_ascii

    def _repr(self, cur_node, cur_height, cur_index, tree_list, height):
        if cur_node == None:
            return
        else:
            tree_list[cur_height][cur_index] = str(cur_node.value)
            self._repr(cur_node.left_child, cur_height + 1, cur_index*2, 
                        tree_list, height)
            self._repr(cur_node.right_child, cur_height + 1, cur_index*2+1, 
                        tree_list, height)
        return tree_list

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            self.size += 1
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
                self.size += 1
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
                self.size += 1
            else:
                self._insert(value, cur_node.right_child)
        else:
            print(f'There is already a node with the value of {value}')

    def build_tree(self, num_nodes=50, max_val=1000):
        from random import randint
        for num in range(num_nodes):
            new_node = randint(0, max_val)
            self.insert(new_node)

    def print_tree(self, traversal_order='inorder'):
        if self.root == None:
            print(f'There is no root of this tree')
        elif traversal_order == 'preorder':
            print('Printing Pre-Order Traversal...')
            self._print_tree_preorder(self.root)
        elif traversal_order == 'inorder':
            print('Printing In-Order Traversal...')
            self._print_tree_inorder(self.root)
        elif traversal_order == 'postorder':
            print('Printing Post-Order Traversal...')
            self._print_tree_postorder(self.root)

    def _print_tree_preorder(self, cur_node):
        if cur_node != None:
            print(cur_node.value)
            self._print_tree_preorder(cur_node.left_child)
            self._print_tree_preorder(cur_node.right_child)

    def _print_tree_inorder(self, cur_node):
        if cur_node != None:
            self._print_tree_inorder(cur_node.left_child)
            print(cur_node.value)
            self._print_tree_inorder(cur_node.right_child)

    def _print_tree_postorder(self, cur_node):
        if cur_node != None:
            self._print_tree_postorder(cur_node.left_child)
            self._print_tree_postorder(cur_node.right_child)
            print(cur_node.value)

    @property
    def height(self):
        if self.root == None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        else:
            left_height = self._height(cur_node.left_child, cur_height + 1)
            right_height = self._height(cur_node.right_child, cur_height + 1)
            return max(left_height, right_height)

    def has_value(self, search_value):
        if self.root == None:
            print("There is no root to this tree.")
        else:
            return self._search(search_value, self.root)
            
    def _has_value(self, search_value, cur_node):
        if cur_node == None:
            return False
        elif search_value == cur_node.value:
            return True
        elif search_value < cur_node.value:
            return self._search(search_value, cur_node.left_child)
        elif search_value > cur_node.value:
            return self._search(search_value, cur_node.right_child)
        else:
            print("An error occurred while searching.")

    def search(self, search_value):
        if self.root == None:
            print("There is no root to this tree.")
        else:
            return self._search(search_value, self.root)
            
    def _search(self, search_value, cur_node):
        if cur_node == None:
            return None
        elif search_value == cur_node.value:
            return cur_node
        elif search_value < cur_node.value:
            return self._search(search_value, cur_node.left_child)
        elif search_value > cur_node.value:
            return self._search(search_value, cur_node.right_child)
        else:
            print("An error occurred while searching.")
    
    def delete(self, node_val):
        node_to_delete = self.search(node_val)

        if node_to_delete == None:
            return "Node not found"
        
        elif node_to_delete.has_no_children():
            if node_to_delete.is_left_child():
                node_to_delete.parent.left_child = None
            elif node_to_delete.is_right_child():
                node_to_delete.parent.right_child = None

        elif node_to_delete.has_one_child():
            if node_to_delete.is_left_child():    
                if node_to_delete.has_left_child():
                    node_to_delete.left_child.parent = node_to_delete.parent
                    node_to_delete.parent.left_child = node_to_delete.left_child
                elif node_to_delete.has_right_child():
                    node_to_delete.right_child.parent = node_to_delete.parent
                    node_to_delete.parent.right_child = node_to_delete.left_child
            elif node_to_delete.is_right_child():
                if node_to_delete.has_left_child():
                    node_to_delete.left_child.parent = node_to_delete.parent
                    node_to_delete.parent.right_child = node_to_delete.left_child
                elif node_to_delete.has_right_child():
                    node_to_delete.right_child.parent = node_to_delete.parent
                    node_to_delete.parent.right_child = node_to_delete.right_child

        elif node_to_delete.has_two_children():
            successor = self.find_successor(node_to_delete, node_to_delete, [])
            self._delete(successor)
            node_to_delete.value = successor.value
                     
    def find_successor(self, node_to_delete, cur_node, node_list):
        if cur_node != None:
            self.find_successor(node_to_delete, cur_node.left_child, node_list)
            if cur_node.value == node_to_delete.value:
                return node_list[-1]
            node_list.append(cur_node)
            self.find_successor(node_to_delete, cur_node.right_child, node_list)
            
    def _delete(self, node_to_delete):
        if node_to_delete.has_no_children():
            if node_to_delete.is_left_child():
                node_to_delete.parent.left_child = None
            elif node_to_delete.is_right_child():
                node_to_delete.parent.right_child = None

        elif node_to_delete.has_one_child():
            if node_to_delete.is_left_child():    
                if node_to_delete.has_left_child():
                    node_to_delete.left_child.parent = node_to_delete.parent
                    node_to_delete.parent.left_child = node_to_delete.left_child
                elif node_to_delete.has_right_child():
                    node_to_delete.right_child.parent = node_to_delete.parent
                    node_to_delete.parent.right_child = node_to_delete.left_child
            elif node_to_delete.is_right_child():
                if node_to_delete.has_left_child():
                    node_to_delete.left_child.parent = node_to_delete.parent
                    node_to_delete.parent.right_child = node_to_delete.left_child
                elif node_to_delete.has_right_child():
                    node_to_delete.right_child.parent = node_to_delete.parent
                    node_to_delete.parent.right_child = node_to_delete.right_child


tree = BST()
nodes = [30, 15, 1, 10, 22, 45, 35, 11, 41, 17, 27, 50, 55, 60, 75, 57, 5, 4, 9, 38, 47,
         33, 0, 43, 44, 42]
for i in nodes:
    tree.insert(i)
print(f'Tree height: {tree.height}    Total nodes: {tree.size}')
print(tree)

del_node_value = 17
del_node = tree.search(del_node_value)
#print(f"Successor of {del_node.value}: {tree.find_successor(del_node, del_node, []).value}")
print(f"Deleting {del_node.value}...")
tree.delete(del_node_value)
print(tree)
print(tree.height)
