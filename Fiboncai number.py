#using for loop fibonaci
#
#prevA= 0
#prevB=1
#print(prevA)
#print(prevB)

#for fibo in range(18):
    #newFibo=prevA+prevB
    #print(newFibo)
    #prevA=prevB
    #prevB=newFibo

    #using recursion in fibonaci
print(0)
print(1)
count = 2

def fibonacci(pre1,pre2):
    global count
    if count <= 19:
        newFibo=pre1+pre2
        print(newFibo)
        prev2=prev1
        prev1=newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)