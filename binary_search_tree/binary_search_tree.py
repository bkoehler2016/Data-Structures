"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value < root, go left
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            # if left child is None
            else:
                # add here
                self.left.insert(value)
                
        
        # if value >= root go right (dupes go to the right)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            
            #if right is None
            else:
                # add here
              self.right.insert(value)
                
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Return True if the tree contains the value
        # False if it does not
        if target is self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        
    # Return the maximum value found in the tree
    def get_max(self):
        # O(n)
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        # O(1)
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        #check for left
        if self.left:
            #for each on left
            self.left.for_each(fn)
            #check for right
        if self.right:
            #for each on right
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        qq = deque()
        qq.append(node)

        while len(qq) > 0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
         stack = Stack()
         stack.push(node)
         while stack.size != 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self,node):
        stack = Stack()
        stack.push(node)
        while stack.size is not 0:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.push(node.right)
                
            if node.left:
                stack.push(node.left)
                

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self is None:
            return
        s1 = []
        s2 = []
        
        s1.append(self)
        
        while s1:
            node = s1.pop()
            s2.append(node)
            
            if node.left:
                s1.append(node.left)
                
            if node.right:
                s1.append(node.right)
                
        while s2:
            node = s2.pop()
            print(node.value)
        
        
                
                

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("BFT")
bst.bft_print(bst)
print("DFT")
bst.dft_print(bst)

print("elegant methods")

print("in order")
bst.in_order_print(bst)

print("pre order")
bst.pre_order_dft(bst)

print("post order")
bst.post_order_dft(bst)
