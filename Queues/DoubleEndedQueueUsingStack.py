class DoubleEndedQueue:
    def __init__(self, size):
        self.size = size
        self.doubleEndedQueue = [None] * size
        self.front = None
        self.rear = None

    def enqueue_using_rear(self, data):
        if self.is_full_rear():
            print("Cannot Insert at Rear End")
        else:
            self.rear = self.rear + 1
            self.doubleEndedQueue[self.rear] = data

    def enqueue_using_front(self, data):
        if self.is_full_front():
            print("Cannot Insert at Front End")
        else:
            self.doubleEndedQueue[self.front] = data
            self.front = self.front - 1

    def dequeue_using_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            item_to_remove = self.doubleEndedQueue[self.rear]
            self.doubleEndedQueue[self.rear] = None
            self.rear = self.rear - 1
            return item_to_remove

    def dequeue_using_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            self.front = self.front - 1
            item_to_remove = self.doubleEndedQueue[self.front]
            self.doubleEndedQueue[self.front] = None
            return item_to_remove

    def peek_at_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.doubleEndedQueue[self.front - 1]

    def peek_at_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.doubleEndedQueue[self.rear]

    def is_empty(self):
        return self.front == self.rear

    def is_full_rear(self):
        return self.rear == (self.size - 1)

    def is_full_front(self):
        return self.front is None
