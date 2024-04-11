#!/usr/bin/python3
# singly_linked_list
class Node:
    """Defines the node of a singly linked list
    
    Args:
        data (int): The value of data to be passed
        next_node (Node): The value of the next node that will be pointed to
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the value of the data private attribute"""
        return self.__data
    
    @data.setter
    def data(self, value):
        """ Set the value of the data private attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the value of the next_node private attribute"""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """ Set the value of the next_node private attribute"""
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        self.head = None
    
    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.head is None:
            new.next_node = None
            self.head = new
        elif self.head.data > value:
            new.next_node = self.head
            self.head = new
        else:
            tmp = self.head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
