import random
from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
        

    # Insert the given value into the tree
    def insert(self, value):
        
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
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

        #while self.right:
        #    self = self.right
        #return self.value
        while self.right:
            return self.right.get_max()
        return self.value        
        """
        The below code is dumb all we need to do is check if the current node has a right hand branch
        if there is a right hand branch we set the current branch to the right hand branch and keep going
        if there is no right hand branch then the current node is larger than the leaves below it and ew need to return the current node
        There is no need for a left right comparison
        """


        """
        if self.right:
            self.right.get_max()
                
        if self.left and not self.right:
            return self.value
        
        #if not self.right or not self.left:
        #    return self.value
        else:
            return self.value
        """
        
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        """base = self
        fn(self.value)
        if base.left:
            fn(base.left.value)
            if base.right:
                fn(base.right.value)
            base.left.for_each(fn)
        if base.right:
            fn(base.right.value)
            if base.left:
                fn(base.left.value)
            base.right.for_each(fn)
        """
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if not self:
            return
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
     
    def bft_print(self):
        
    
        qq = deque()
        qq.append(self)

        while len(qq) >  0:
            current = qq.popleft()
            print(current.value)
            if current.left:
                qq.append(current.left)
            if current.right:
                qq.append(current.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        #self.dft_print()
        """
        s = []
        s.append(self)
        
        while len(s) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)
        """
        if not self:
            return
        print(self.value)
        if self.left:
            self.left.dft_print()
        if self.right:
            self.right.dft_print()
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
    # we need to print the node, the left and the right 
        if not self:
            return
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        
    #print the left, then the right, then the node
        
        if not self:
            return
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


    def in_order_dft(self):
        #print left, self, right
        if not self:
            return
        if self.left:
            self.left.in_order_dft()
        print(self.value)
        if self.right:
            self.right.in_order_dft()