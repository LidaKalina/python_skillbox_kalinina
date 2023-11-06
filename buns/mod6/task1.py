class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def get(self, index):
        curr_node = self.head
        for i in range(index):
            if curr_node is None:
                raise IndexError("Index out of range")
            curr_node = curr_node.next
        if curr_node is None:
            raise IndexError("Index out of range")
        return curr_node.data

    def remove(self, index):
        if index == 0:
            if self.head is None:
                raise IndexError("Index out of range")
            self.head = self.head.next
        else:
            prev_node = None
            curr_node = self.head
            for i in range(index):
                if curr_node is None:
                    raise IndexError("Index out of range")
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node is None:
                raise IndexError("Index out of range")
            prev_node.next = curr_node.next

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = None
            curr_node = self.head
            for i in range(n):
                if curr_node is None:
                    raise IndexError("Index out of range")
                prev_node = curr_node
                curr_node = curr_node.next
            if curr_node is None:
                raise IndexError("Index out of range")
            prev_node.next = new_node
            new_node.next = curr_node

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node.data
            curr_node = curr_node.next

