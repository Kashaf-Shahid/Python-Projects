class stack:
  def __init__(self):
   self.values=[]   #create empty list
   #applying method
  def push(self,x):   #x is simple argument
    self.values= [x]+self.values
  def pop(self):
               return self.values.pop(0)
  
s=stack()        #object
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.values)
print(s.pop())
  
