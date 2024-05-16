class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return 7 - (key % 7)

    def insert(self, key, value):
        index = self.hash_function_1(key)
        if index is None:
            return
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
            return
        else:
            offset = self.hash_function_2(key)
            i = 1
            while True:
                new_index = (index + offset * i) % self.size
                if new_index == index:
                    return
                if self.keys[new_index] is None:
                    self.keys[new_index] = key
                    self.values[new_index] = value
                    return
                i = i + 1

    def search(self, key):
        index = self.hash_function_1(key)
        if index is None:
            return None
        if self.keys[index] == key:
            return self.values[index]
        else:
            offset = self.hash_function_2(key)
            i = 1
            while True:
                new_index = (index + offset * i) % self.size
                if new_index == index:
                    return None
                if self.keys[new_index] == key:
                    return self.values[key]
                i = i + 1

    def delete(self, key):
        index = self.hash_function_1(key)
        if index is None:
            return
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None
            return
        else:
            offset = self.hash_function_2(key)
            i = 1
            while True:
                new_index = (index + offset * i) % self.size
                if new_index == index:
                    return
                if self.keys[new_index] == key:
                    self.keys[new_index] = None
                    self.values[new_index] = None
                    return
                i = i + 1
