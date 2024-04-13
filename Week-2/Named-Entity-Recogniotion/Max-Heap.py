class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insertKey(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def increaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extractMax(self):
        if len(self.heap) <= 0:
            return float("-inf")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.maxHeapify(0)
        return root

    def maxHeapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)
    def displayHeap(self):
        print(self.heap)

# Example usage:
max_heap = MaxHeap()
max_heap.insertKey(3)
max_heap.insertKey(2)
max_heap.insertKey(15)
max_heap.insertKey(5)
max_heap.insertKey(4)
max_heap.insertKey(45)

max_heap.displayHeap()
print(max_heap.extractMax())  # Should return 45, the maximum element
