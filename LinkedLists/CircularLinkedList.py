class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            if self.head is not None:
                new_node.next = self.head
            else:
                new_node.next = new_node
            self.head = new_node
            return
        current_node = self.head
        position = 0
        while current_node.next != self.head and (position + 1) < index:
            current_node = current_node.next
            position = position + 1
        if (position + 1) == index:
            new_node.next = current_node.next
            current_node.next = new_node
            return
        print("Index Out of Range")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def update_node_at_index(self, data, index):
        if index == 0 and self.head is not None:
            self.head.data = data
        else:
            current_node = self.head
            position = 0
            while current_node != self.head and position != index:
                current_node = current_node.next
                position = position + 1
            if current_node != self.head:
                current_node.data = data
            else:
                print("Index Out Of Range")

    def remove_first(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head.data = None
            return
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = self.head.next
        self.head = self.head.next

    def remove_at_index(self, index):
        if self.head is None:
            return
        if self.head.next == self.head and index == 0:
            self.head.data = None
            return
        current_node = self.head
        position = 0
        while current_node.next != self.head and (position + 1) < index:
            current_node = current_node.next
            position = position + 1
        if (position + 1) == index:
            current_node.next = current_node.next.next
            return
        print("Index Out Of Range")

    def remove_at_last(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next != self.head:
            current_node = current_node.next
        current_node.next = self.head

    def size_of_circular_linked_list(self):
        if self.head is None:
            return 0
        if self.head.next == self.head:
            return 1
        size = 2
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
            size = size + 1
        return size

    def print_circular_linked_list(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            print(self.head.data)
            return
        current_node = self.head
        while current_node.next != self.head:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
