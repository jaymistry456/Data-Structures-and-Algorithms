# Initially, front and rear will point at the first index (0) with all the
# indexes set to None value.
#
# While inserting an element at the front, the element will be inserted at
# the current front index first and then the front index will be decremented.
#
# While deleting from the front, the front pointer will be incremented first
# and then the element at the front pointer will be set to None.
#
# While inserting at the rear index, the rear will be incremented first and
# then the value is inserted at the rear pointer.
#
# While deleting from the rear pointer, the current rear pointer will be set
# to None first and then the rear pointer will be decremented.

class MyCircularDeque:

    def __init__(self, k: int):
        self.circular_deque = [None] * k
        self.front = 0
        self.rear = 0
        self.size = k

    def insert_front(self, value: int) -> bool:
        if self.is_full():
            return False
        self.circular_deque[self.front] = value
        self.front = (self.front - 1) % self.size
        return True

    def insert_rear(self, value: int) -> bool:
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.size
        self.circular_deque[self.rear] = value
        return True

    def delete_front(self) -> bool:
        if self.is_empty():
            return False
        self.front = (self.front + 1) % self.size
        self.circular_deque[self.front] = None
        return True

    def delete_rear(self) -> bool:
        if self.is_empty():
            return False
        self.circular_deque[self.rear] = None
        self.rear = (self.rear - 1) % self.size
        return True

    def get_front(self) -> int:
        if self.is_empty():
            return -1
        return self.circular_deque[(self.front + 1) % self.size]

    def get_rear(self) -> int:
        if self.is_empty():
            return -1
        return self.circular_deque[self.rear]

    def is_empty(self) -> bool:
        return self.front == self.rear and self.circular_deque[self.front] is None

    def is_full(self) -> bool:
        return self.circular_deque[self.front] is not None
