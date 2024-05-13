class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, item):
        if self.is_full():
            print("Stack is full")
            return
        self.top = self.top + 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        item = self.stack[self.top]
        self.top = self.top - 1
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        else:
            return self.stack[-1]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == (self.size - 1)
