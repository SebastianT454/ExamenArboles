class Node_ArbolGeneral:
  def __init__(self, value):
    self.value = value
    self.children = []

class GeneralTree:
  def __init__(self):
    self.root = None

  def insert(self, value, parent=None, current=None):
    if(current is None):
      current = self.root
    if(current):
      if(current.value == parent):
        current.children.append(Node_ArbolGeneral(value))
      else:
        for child in current.children:
          self.insert(value, parent, child)
    else:
      self.root = Node_ArbolGeneral(value)

  def traverse(self, current):
    if(current is not None):
      print(current.value)
      for child in current.children:
        self.traverse(child)

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

#Árbol binario de búsqueda
class BST:
  def __init__(self, data):
    self.root = None
    self.populate_tree(data)

  def populate_tree(self, data):
    for value in data:
      self.insert(value, self.root)

  def print_tree(self, node=None, prefix="", is_left=True):#Asuma que todo árbol tendrá al menos un elemento -> con 0, tendrán que agregar un flag para evitar recursión infinita
    if not node:
      self.print_tree(self.root)
      return
    if node.right:
      self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
      self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

  def insert(self, value, current):
    if(self.root is None):
      self.root = Node(value)
      return
    if(current.value == value):
      return
    elif(value > current.value):
      if(current.right is None):
        current.right = Node(value)
        return
      else:
        self.insert(value,current.right)
    else:
      if(current.left is None):
        current.left = Node(value)
        return
      else:
        self.insert(value,current.left)

#Árbol binario
class BT:
  def __init__(self, data):
    self.root = None
    self.populate_tree(data)

  def populate_tree(self, data):
    for value in data:
      self.insert(value, [self.root])

  def print_tree(self, node=None, prefix="", is_left=True): #Asuma que todo árbol tendrá al menos un elemento -> con 0, tendrán que agregar un flag para evitar recursión infinita
    if not node:
      self.print_tree(self.root)
      return
    if node.right:
      self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    if node.left:
      self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

  def insert(self, value, q):
    if(self.root):
      if(q):
        root = q.pop(0)
        if(root.left):
          q.append(root.left)
        else:
          root.left = Node(value)
          return "Ok!"

        if(root.right):
          q.append(root.right)
        else:
          root.right = Node(value)
          return "Ok!"     
        self.insert(value,q) 
    else:
      self.root = Node(value)


def dfs_bst(node):
    if node is not None:
        dfs_bst(node.left)
        print(node.value, end=" ")
        dfs_bst(node.right)

from collections import deque

def bfs_bt(node):
    if node is not None:
        queue = deque()
        queue.append(node)

        while queue:
            current = queue.popleft()
            print(current.value, end=" ")

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

#E1:

def find_sibling_of_min(bst_tree):
    if bst_tree.root is None:
        return None  # El árbol está vacío

    # Encuentra el nodo menor en el árbol (el nodo más a la izquierda)
    current = bst_tree.root
    while current.left is not None:
        current = current.left

    # Verifica si el nodo menor tiene un hermano en el subárbol derecho
    if current.right is not None:
        return current.right
    else:
        return None
    
#E2:

def count_value_excluding_parent_of_leaves(self, value):
    def count_recursively(node, value):
        if node is None:
            return 0

        count_left = count_recursively(node.left, value)
        count_right = count_recursively(node.right, value)

        if node.left is None and node.right is None:
            return count_left + count_right
        else:
            return count_left + count_right + (node.value == value)

    return count_recursively(self.root, value)

#E3:

def are_left_and_right_subtrees_equal(self):
    def is_equal(node1, node2):
            # Caso base: si ambos nodos son None, son iguales.
        if node1 is None and node2 is None:
            return True
            # Si uno de los nodos es None y el otro no, no son iguales.
        if node1 is None or node2 is None:
            return False
            # Verificar si los valores de los nodos son iguales.
        if node1.value != node2.value:
            return False
            # Recursivamente, verificar los subárboles izquierdo y derecho.
        return is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)

    if self.root is None:
        return True  # Si el árbol está vacío, se consideran iguales.

    return is_equal(self.root.left, self.root.right)

#E4:

def update_values(tree):
  if tree is None:
    return None

  # Actualiza el valor del nodo actual con la sumatoria de sus hijos.

  tree.value = sum(update_values(child) for child in (tree.left, tree.right))

  # Actualiza los valores de los hijos del nodo actual.

  return tree