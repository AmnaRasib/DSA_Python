class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        current=len(self.heap)-1 #index of the last element
        while current >0:
            parent=(current-1)//2
            if self.heap[current] > self.heap[parent]:
                self.heap[current],self.heap[parent]=self.heap[parent],self.heap[current]
                current=parent
            else:
                break
    def show_heap(self):
        print("Heap: ",self.heap)
# Example
heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(3)
heap.insert(2)
heap.insert(8)
heap.show_heap()
    