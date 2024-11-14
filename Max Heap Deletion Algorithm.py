class Heap:
    def __init__(self, capacity):
        self.array = [0] * capacity  
        self.capacity = capacity 
        self.size = 0  


    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]


    def heapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2


        if left < self.size and self.array[left] > self.array[largest]:
            largest = left


        if right < self.size and self.array[right] > self.array[largest]:
            largest = right


        if largest != i:
            self.swap(i, largest)
            self.heapify(largest)


    def insert(self, value):
        if self.size == self.capacity:
            print("Heap is full. Cannot insert more elements.")
            return


        i = self.size
        self.size += 1
        self.array[i] = value


        while i != 0 and self.array[(i - 1) // 2] < self.array[i]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2


    def deleteMax(self):
        if self.size == 0:
            print("Heap is empty. Cannot extract maximum element.")
            return -1


        max_value = self.array[0]


        self.array[0] = self.array[self.size - 1]
        self.size -= 1


        self.heapify(0)
        return max_value


    def printHeap(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()


    def destroyHeap(self):
        self.array = []
        self.size = 0


heap = Heap(10)
heap.insert(35)
heap.insert(33)
heap.insert(42)
heap.insert(10)
heap.insert(14)
heap.insert(19)
heap.insert(27)
heap.insert(44)
heap.insert(26)
heap.insert(31)


print("Heap elements before deletion:", end=" ")


heap.printHeap()
max_value = heap.deleteMax()


print("Maximum element:", max_value)
print("Heap elements after deletion:", end=" ")


heap.printHeap()
heap.destroyHeap()