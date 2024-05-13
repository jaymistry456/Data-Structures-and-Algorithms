class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleEndedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_using_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.rear = new_node
            self.front = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def enqueue_using_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def dequeue_using_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            node_to_remove = self.rear
            self.rear = self.rear.prev
            if self.rear is None:
                self.front = None
            else:
                self.rear.next = None
            return node_to_remove.data

    def dequeue_using_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            node_to_remove = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            return node_to_remove.data

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
