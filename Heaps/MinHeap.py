class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._percolate_up(parent_index)

    def delete(self):
        if len(self.heap) == 0:
            return
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return min_value

    def _percolate_down(self, index):
        smallest = index
        left_child = smallest * 2 + 1
        right_child = smallest * 2 + 2
        # Finding which one is the smallest out of index and its left and right children
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < left_child(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._percolate_down(smallest)

    def heapify(self, arr):
        self.heap = arr
        for i in range((len(arr) // 2 - 1) - 1, -1, -1):
            self._percolate_down(i)
