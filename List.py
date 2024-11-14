l = []
for i in range(10):
    if i%2:
        l.append(i)
print(l)

#Using List Comprehension:
ls = [i for i in range(10) if i%2]
print(ls)

