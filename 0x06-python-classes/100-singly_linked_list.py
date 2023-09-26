#!/usr/bin/python3
""" Task 7 """

class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Constructor"""
        if type(data) is int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            self.__next_node = None
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
        
    @property
    def next_node(self):
        """Getter for next_node"""
        return self.next_node

    @data.setter
    def next_node(self, value):
        """Setter for next_node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Constructor"""
        self.__head = None

    def __str__(self):
        """Function to display the list"""
        node = self.__head
        while node is not None:
            print(node.data)
            node = node.next_node

    def sorted_insert(self, value):
        """Function to add to the list"""
        node = self.__head
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        while node:
            next_node = node.next_node
            if next_node and next_node.data < value:
                node = next_node
            else: 
                new_node.next_node = node.next_node
                node.next_node = new_node
