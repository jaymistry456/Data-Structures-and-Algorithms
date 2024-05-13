class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        else:
            top_node = self.top
            top_node.next = None
            self.top = self.top.next
            return top_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        else:
            return self.top.data

    def is_empty(self):
        return self.top is None
