class MinHeap:
    def __init__(self):
        self.heap = []
    def parent(self, i):
        return int((i-1)/2)
    def left(self, i):
        return 2*i+1
    def rigth(self, i):
        return 2*i+2
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
    def get_min(self):
        return self.heap[0]
    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap)-1
        while (i != 0) & (self.heap[i] < self.heap[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)
    def min_heapify(self, i):
        length = len(self.heap)
        key_min = i
        if self.left(i) < length:
            if self.heap[key_min] > self.heap[self.left(i)]:
                key_min = self.left(i)
        if self.rigth(i) < length:
            if self.heap[key_min] > self.heap[self.rigth(i)]:
                key_min = self.rigth(i)
        if key_min != i:
            self.swap(key_min, i)
            self.min_heapify(key_min)
    def update_key(self, k, new_val):
        if new_val > self.heap[k]:
            self.heap[k] = new_val
            self.min_heapify(k)
        if new_val < self.heap[k]:
            self.heap[k] = new_val
            while (k != 0) & (self.heap[k] < self.heap[self.parent(k)]):
                self.swap(k, self.parent(k))
                k = self.parent(k)
    def extract_min(self):
        length = len(self.heap)
        if length == 1:
            self.heap = []
            return
        if length > 1:
            self.heap[0] = self.heap[length-1]
            del self.heap[-1]
            self.min_heapify(0)
    def delete(self, k):
        self.update_key(k, float('-inf'))
        self.extract_min()

heap = MinHeap()
lists = [5, 10, 1, 8, 7, 1]
for data in lists:
    heap.insert(data)
print(heap.heap)
heap.update_key(1, 0)
print(heap.heap)
heap.extract_min()
print(heap.heap)
heap.delete(1)
print(heap.heap)
