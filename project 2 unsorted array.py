class ArrayOperations:
    def __init__(self):
        self.array = []  

    def stack_push(self, value):
        self.array.append(value)  
        print(f"Stack Push: {value}")
    
    def stack_pop(self):
        if len(self.array) == 0:
            print("Stack is empty")
            return None
        value = self.array.pop()  
        print(f"Stack Pop: {value}")
        return value

    def queue_enqueue(self, value):
        self.array.append(value)  
        print(f"Queue Enqueue: {value}")
    
    def queue_dequeue(self):
        if len(self.array) == 0:
            print("Queue is empty")
            return None
        value = self.array.pop(0)  
        print(f"Queue Dequeue: {value}")
        return value

    def display(self):
        print(f"Current array: {self.array}")


operations = ArrayOperations()

operations.stack_push(1)
operations.stack_push(2)
operations.stack_pop()
operations.display()

operations.queue_enqueue(1)
operations.queue_enqueue(2)
operations.queue_dequeue()
operations.display()
