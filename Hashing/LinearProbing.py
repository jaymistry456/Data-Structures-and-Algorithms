class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if index is None:
            return
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
            return
        else:
            new_index = (index + 1) % self.size
            while new_index != index:
                if self.keys[new_index] is None:
                    self.keys[new_index] = key
                    self.values[new_index] = value
                    return
                new_index = (new_index + 1) % self.size
            print("Hash Table is full")
            return

    def search(self, key):
        index = self.hash_function(key)
        if index is None:
            return None
        if self.keys[index] == key:
            return self.values[index]
        else:
            new_index = (index + 1) % self.size
            while new_index != index and self.keys[new_index] is not None:
                if self.keys[new_index] == key:
                    return self.values[new_index]
                new_index = (new_index + 1) % self.size
            return None

    def delete(self, key):
        index = self.hash_function(key)
        if index is None:
            return
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
            return
        else:
            new_index = (index + 1) % self.size
            while new_index != index and self.keys[new_index] is not None:
                if self.keys[new_index] == key:
                    self.keys[new_index] = None
                    self.values[new_index] = None
                    self.rehash()
                    return
                new_index = (new_index + 1) % self.size

    def rehash(self):
        # Doubling the Hash table size
        self.size = self.size * 2
        old_keys = self.keys
        old_values = self.values
        self.keys = [None] * self.size
        self.values = [None] * self.size
        # Inserting all the old (key, value) pairs into new Hash table
        for key, value in zip(old_keys, old_values):
            if key is not None:
                self.insert(key, value)
