# In this class we make a empty heap
class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = self.parent = self.child = None
        self.degree = 0
        # checks if the parent losses any child or not needthis later to marks the nodes
        self.mark = False

# In this class we initilize the root and apply fibonacci operations through circular link list


class Fibonacci_heap:
    def __init__(self):
        self.root = None
        self.no_total_node = 0
        self.H_min = None

    # in this operation the node is to be insert in rootlist
    def Insert(self, value):
        self.node = Node(value)
        # since its a circular link list the left side of the node = right side of the node
        self.node.right = self.node.left = self.node
        # if the linklist is empty then root becomes node
        if self.root == None:
            self.root = self.node
        # if the linklist is not empty insert a node in root list
        else:
            self.node.right = self.root.right
            self.node.left = self.root
            self.node.right.left = self.node
            self.root.right = self.node

#  setting Hmin pointer towards the minimum mode of the heap if hmin is none then hmin is equal to the first node
# other wise it points towards that node whose value is minimum

        if self.H_min is None or self.node.value < self.root.value:
            self.H_min = self.node

        # count the total no of nodes in link list
        self.no_total_node += 1

# we find the minimum node here and we can simply do it by returning the Hmin pointer which points
#  towards the minimum node
    def Find_Minimum_Node(self):
        return self.H_min

    # In this operation we merge two heaps and return a single heap
    # This means gets a union of two  heap
    def Union(self, H2):
        # H1 is a object of fibonacci heap this is one heao
        H1 = Fibonacci_heap
    # H2 is another object of fibonacci heap and this is another heap and merge these two heaps using circular link list
        H1.root = self.root
        H1.H_min = self.H_min
        h = H2.root.left
        h = H1.root.left
        H1.root.left = h
        H1.root.left.right = H1.root

        if H2.H_min.value < H1.H_min.value:  # Update the min pointer
            H1.H_min = H2.H_min

        # total no nodes having the nodes of H1 and H2
        total_nodes = self.no_total_node + H2.no_total_node
        return H1

    # make the child list of the root list
    def make_child_list(self, parent, child_node):
        if parent.child == None:       # if there is no child then the child_node becomes the child node
            parent.child = child_node

        else:  # else insert the child node in child list using circular link list
            child_node.right = parent.child.right
            child_node.left = parent.child
            parent.child.right.left = child_node
            parent.child.right = child_node

    # remove the node from linklist root list
    def Delete_node(self, node):
        if node == self.root:
            self.root = node.right
        node.left.right = node.right
        node.right.left = node.left
        node = None

    # this operation makes the y node no longer a root list root
    def Fib_Heap_link(self, y, x):
        self.Delete_node(y)  # this delete the root list y node
        y.left = y
        y.right = y
        self.make_child_list(x, y)          # make y a child node of x
        x.degree += 1                    # as the child of x increases the degree also increases
        y.parent = x
        y.mark = False

    # This operation can be done when you have to remove a child node from child list
    def delete_child_node(self, parent, node):
        if parent.child == parent.child.right:
            parent.child = None
        elif parent.child == node:
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left

# this operation applys when the child node becomes smaller than its parent node
#   then the link between parent and child should be cut and child should me merge in root list
    def Cut(self, x, y):
        # delete the child node from child list or you may say cut the link between child and parent node
        self.delete_child_node(y, x)
        # after deleting child decrease the degree of parent node
        y.degree -= 1
        # insert the child in root list
        self.Insert(y)
        # after inserting child into root list there will be no parent of x
        x.parent = None
        # mark it false b/c it doesn't loose any of its child
        x.mark = False

    # after cutting the link b/w child and parent node, if parent was'nt mark we mark the parent
    # else we cut the link b/w parent and grandparent node
    def Cascading_Cut(self, y):
        z = y.parent
        if z != None:
            # if parent isnn't mark mark the parent
            if y.mark == False:
                y.mark = True
            else:
                # else cut the link b/w parent and grandparent node
                self.Cut(y, z)
                # and then mark the grandparent node
                self.Cascading_Cut(z)

    # this operation is done when the value of node decreases or we decreases the node value

    def Decrease_Node(self, x, value):
        if value > x.value:
            raise "New value is greater then current node value"
        # if it doesn't voilate the min heap property then simply makes the new value a node value
        x.value = value
        y = x.parent
        # if it voilates the min heap property that parent value is greater than child value
        if y != None and x.value < y.value:
            self.Cut(x, y)  # cut the link
            # mark it if not marked or cut the link b/w parent and grandparent node
            self.Cascading_Cut(y)
        # update the min pointer if required
        if x.value < self.H_min.value:
            self.H_min = x
