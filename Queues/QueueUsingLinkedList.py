class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            node_to_remove = self.front
            self.front = self.front.next
            data = node_to_remove.data
            return data

    def peek_at_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.front.data

    def peek_at_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.rear.data

    def is_empty(self):
        return self.front is None
