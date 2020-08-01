class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        """
        Don't need to move the list items, just the "next" pointers
        So we need to know what node that we're on = current
        what node comes next = nextnode or next_node
        and what node came before = prev_node

        we start at the head, current is the head, there is no previous
        start loop
        on the head of the list, change current.prev to current.next
        change the previous node to the current node, starting to shuffle through
        and then change the current node to the next node
        This way we iterate through the list and change the pointers

         [] -> [] -> [] ->
         <-[] -> [] -> []
         <-[] <- [] -> []
        and so on
        

        """
        
        current = self.head
        previous_node = None
        
        if not current:
            return
        while current:
            next_node = current.get_next()
            current.next_node = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node


                
