class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.circularQueue = [None] * size
        self.front = None
        self.rear = None

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return
        else:
            self.rear = (self.rear + 1) % self.size
            self.circularQueue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            self.front = (self.front + 1) % self.size
            item = self.circularQueue[self.front]
            self.front = None
            return item

    def peek_at_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.circularQueue[self.front + 1]

    def peek_at_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.circularQueue[self.rear]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return ((self.rear + 1) % self.size) == self.front
