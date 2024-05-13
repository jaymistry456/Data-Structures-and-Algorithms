class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return
        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            item = self.queue[self.front]
            self.front = self.front + 1
            return item

    def peek_at_front(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.queue[self.front + 1]

    def peek_at_rear(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        else:
            return self.queue[self.rear]

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == (self.size - 1)
