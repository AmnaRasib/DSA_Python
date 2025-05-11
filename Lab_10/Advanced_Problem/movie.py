class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, movie):
        self.heap.append(movie)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index].rating > self.heap[parent].rating:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def get_top_movie(self):
        if self.heap:
            return self.heap[0].title, self.heap[0].rating
        return None, None

    def remove_top_movie(self):
        if len(self.heap) > 1:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            top_movie = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            top_movie = self.heap.pop()
        else:
            return None
        return top_movie.title, top_movie.rating

    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left].rating > self.heap[largest].rating:
                largest = left
            if right < size and self.heap[right].rating > self.heap[largest].rating:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# Example Usage
max_heap = MaxHeap()
max_heap.insert(Movie("Movie A", 7))
max_heap.insert(Movie("Movie B", 9))
max_heap.insert(Movie("Movie C", 10))
max_heap.insert(Movie("Movie D", 8))

print("Top Movie:", max_heap.get_top_movie())

print("\nRemoving top movie...")
print("Removed Movie:", max_heap.remove_top_movie())

print("\nTop Movie after Removal:", max_heap.get_top_movie())