import random
import time
n=int(input("enter the size"))
a=[random.randint(0,100) for i in range(n)]
#a=[int(i) for i in input().split()]
def merge(a,b,k=0):
    i,j,c=0,0,[]
    #print(a,b)
    while((i<len(a)) and (j<len(b))):
        if (a[i]<b[j]):
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
            k=k+len(a)-i
    while(i<len(a)):
        c.append(a[i])
        i=i+1
    while(j<len(b)):
        c.append(b[j])
        j=j+1
    return c,k
def merge_sort(a,k):
    if(len(a)>1):
        a1,k=merge_sort(a[0:len(a)//2],k)
        b1,k=merge_sort(a[len(a)//2:],k)
        a,k=merge(a1,b1,k)
    return a,k
print(a)
start=time.clock()
print("count :",merge_sort(a,0)[1])
print(time.clock()-start)
