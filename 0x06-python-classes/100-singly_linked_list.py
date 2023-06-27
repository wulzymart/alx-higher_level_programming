#!/usr/bin/python3
"""Defines class for node and singly linked list"""


class Node:
    """The node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """initializes a the node of a singly linked list
        Arguements:
        data: data in the node
        next_node: the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets private attribute 'data'"""
        return self.__data

    @data.setter
    def data(self, data):
        """sets private attribute 'data'"""
        if isinstance(data, int) or data is None:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """gets private attribute 'next_node'"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets private attribute 'next_node'"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class for a singly linked list of integers"""
    def __init__(self):
        """Initializes the singly linked list head node"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the list in a sorted manner"""
        node = Node(value)
        node.next_node = None

        if not self.__head:
            self.__head = node
            return
        head = self.__head
        if self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
            return
        prev = head
        while head:
            if head.data > value:
                node.next_node = head
                prev.next_node = node
                return
            prev = head
            head = head.next_node
        prev.next_node = node

    def __str__(self):
        """prints all data in the linked list"""
        datas = []
        head = self.__head
        while head:
            datas += [str(head.data)]
            head = head.next_node
        return "\n".join(datas)
