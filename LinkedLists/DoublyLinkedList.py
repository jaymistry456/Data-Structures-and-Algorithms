class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if self.head is None:
            if index == 0:
                self.insert_at_beginning(data)
                return
        current_node = self.head
        position = 0
        while current_node is not None and (position + 1) < index:
            current_node = current_node.next
            position = position + 1
        if (position + 1) == index:
            new_node.next = current_node.next
            new_node.prev = current_node
            if current_node.next is not None:
                current_node.next.prev = new_node
            current_node.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.insert_at_beginning(data)
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def update_node_at_index(self, data, index):
        if self.head is None:
            return
        if self.head == self.tail and index == 0:
            self.head.data = data
            return
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            current_node = current_node.next
            position = position + 1
        if position == index:
            current_node.data = data
        print("Index Out Of Range")

    def remove_first(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        if self.head == self.tail:
            if index == 0:
                self.head = None
                self.tail = None
                return
            else:
                print("Index Out Of Range")
                return
        current_node = self.head
        position = 0
        while current_node is not None and (position + 1) != index:
            current_node = current_node.next
            position = position + 1
        if (position + 1) == index:
            if position == 1:
                self.head.next = current_node.next
                current_node.next.prev = self.head
            elif current_node == self.tail:
                self.remove_at_last()
            else:
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            return
        print("Index Out Of Range")

    def remove_at_last(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def size_of_doubly_linked_list(self):
        if self.head is None:
            return 0
        if self.head == self.tail:
            return 1
        current_node = self.head
        size = 1
        while current_node is not None:
            current_node = current_node.next
            size = size + 1
        return size

    def print_doubly_linked_list(self):
        if self.head is None:
            return
        if self.head == self.tail:
            print("head <-> ", self.head.data, " <-> tail")
            return
        current_node = self.head
        print("head <-> ", end='')
        while current_node is not None:
            print(current_node.data, " <-> ")
            current_node = current_node.next
        print("tail")
