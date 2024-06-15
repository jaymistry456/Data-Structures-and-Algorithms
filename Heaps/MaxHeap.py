class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._percolate_up(parent_index)

    def delete(self):
        if len(self.heap) == 0:
            return
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return max_value

    def _percolate_down(self, index):
        largest = index
        left_child = index * 2 + 1
        right_child = index * 2 + 2
        # Finding which one is the largest out of index and its left and right children
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._percolate_down(largest)

    def heapify(self, arr):
        self.heap = arr
        # range starts from the last parent node which is at the middle of the array
        # and goes till index 0 (the second -1), the third -1 is to move the loop in reverse
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            self._percolate_down(i)
