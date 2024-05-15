class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashChaining:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Taking size of the hash table for the hash function
    # If the size of the hash table is 20, hash function will be key % 20
    def hash_function(self, key):
        return key % self.size

    def insert(self, key, val):
        index = self.hash_function(key)
        new_node = Node(key, val)
        if self.table[index] is None:
            self.table[index] = new_node
            return
        prev_node = None
        current_node = self.table[index]
        while current_node is not None and current_node.key < key:
            prev_node = current_node
            current_node = current_node.next
        if prev_node is None:
            new_node.next = current_node
            self.table[index] = new_node
        else:
            prev_node.next = new_node
            new_node.next = current_node

    def search(self, key):
        index = self.hash_function(key)
        current_node = self.table[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current_node = self.table[index]
        prev_node = None
        if current_node is None:
            return
        if current_node.key == key:
            self.table[index] = current_node.next
            return
        while current_node is not None:
            if current_node.key == key:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
