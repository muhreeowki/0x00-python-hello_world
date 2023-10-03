#!/usr/bin/python3
""" Task 7 """


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Constructor"""
        if isinstance(data, int):
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
        nums = []
        node = self.__head
        while isinstance(node, Node):
            nums.append(str(node.data))
            node = node.next_node
        return "\n".join(nums)

    def add_end(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        node = self.__head

        while isinstance(node.next_node, Node):
            node = node.next_node

        node.next_node = Node(value)
        print(value)

    def sorted_insert(self, value):
        """Function to add to the list"""

        if self.__head is None:
            self.__head = Node(value)
            return

        if self.__head.data >= value:
            self.__head = Node(value, self.__head)
            return

        next_node = self.__head.next_node
        while next_node is not None:
            next_node = curr_node.next_node
            if curr_node.data < value:
                curr_node = next_node
            else:
                curr_node.next_node = Node(value, curr_node.next_node)
                break
