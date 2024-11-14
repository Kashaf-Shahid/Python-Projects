d = {}
for i in range(1,10):
 square_value = i*i
d[i] = i*i
print(d)

#Using Dict Comprehension:
d1={n:n*n for n in range(1,10)}
print (d1)
