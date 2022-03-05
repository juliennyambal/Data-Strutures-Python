a = [1,3,2,6,44,34,8,7, 100]

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

    
    
class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None

        
    def build_forward(self, list_item: []):
        """
        The linked list will be populated in order or in a forward manner
        Parameters
        ----------
        list_item : []
            List of items to insert in the list.

        Returns
        -------
        Linked List with all the items from the list of items

        """
        idx = 0
        while idx < len(a):
            new_node = Node(a[idx])
            if self.first is None:
                self.first = new_node
                self.last = new_node
            else:
                self.last.link = new_node
                self.last = new_node
            idx = idx + 1
        return self
    
    def build_backward(self, list_item: []):
        """
        The linked list will be populated in reverse or in a backward manner
        Parameters
        ----------
        list_item : []
            List of items to insert in the list.

        Returns
        -------
        Linked List with all the items from the list of items

        """
        idx = 0
        while idx < len(a):
            new_node = Node(a[idx])
            if self.first is None:
                self.first = new_node
                self.last = new_node
            else:
                new_node.link = self.first
                self.first = new_node
            idx = idx + 1
        return self
    
    def traverse_list(self):
        # Tranverse and print
        current = self.first
        while current != None:
            print(current.data, end=" ")
            current = current.link
        
    def insert_last(self, value_insert):
        # Traverse and insert at the tail of the list
        current = self.first
        while current.link != None:
            current = current.link
        new_node = Node(value_insert)
        current.link = new_node

    def insert_middle(self, value_insert, after):
        """
        Parameters
        ----------
        value_insert : int
            Value to insert in the linked list.
        before : int
            Value to which we need the insert after.
        Returns
        -------
        Self.

        """
        # Inserting 35 after 34 in a list like this 1 3 2 6 44 34 8 7 100 103
        current = self.first
        while current.data != after:
            current = current.link
        new_node = Node(value_insert)
        q = current.link
        current.link = new_node
        new_node.link = q

    def delete_node(self, value):
        current = self.first
        while current.link.data != value:
            current = current.link
        # Next item in the list after the value
        q = current.link.link
        # Item in the list before the value
        p = current
        p.link = q
        
        


new_list = LinkedList()
lst = new_list.build_forward(a)
lst.insert_last(1000)
lst.insert_middle(343, 100)
lst.traverse_list()
print()
lst.delete_node(34)
lst.traverse_list()











                
        
    
