class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1  # index of the new value

        while current > 0:
            parent = (current - 1) // 2
            if self.heap[current] < self.heap[parent]:  # For Min Heap
                self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]
                current = parent
            else:
                break

    def delete_min(self):
        if len(self.heap) == 0:
            return None

        min_value = self.heap[0]  # Save the min (root)
        self.heap[0] = self.heap[-1]  # Replace root with last element
        self.heap.pop()  # Remove last

        current = 0
        size = len(self.heap)

        while True:
            left = 2 * current + 1
            right = 2 * current + 2
            smallest = current

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != current:
                self.heap[current], self.heap[smallest] = self.heap[smallest], self.heap[current]
                current = smallest
            else:
                break

        return min_value

    def show_heap(self):
        print("Heap:", self.heap)


# Test
heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(3)
heap.insert(2)
heap.insert(8)
heap.show_heap()

deleted = heap.delete_min()
print("Deleted:", deleted)
heap.show_heap()
