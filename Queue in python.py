class queue: #queue
 def __init__(self): 
  self.values=[] #list is simple a collection of elements
def enqueue(self,x):
 self.values.append(x)
def dequeue(self):
 front = self.values[0]
 self.values = self.values[1:] #slicing
 return front 

q1=queue()  #object
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.values)
print(q1.dequeue())
print(q1.values)

