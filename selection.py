from random import randint
import time
n=int(input("Enter no of elements :"))
a=[randint(0,100) for i in range(n)]
print(a)
start=time.clock();
for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        if a[min]>a[j]:
            min=j
    temp=a[min]
    a[min]=a[i]
    a[i]=temp

print("Sorted :")
print(a)
print('%f'%(time.clock()-start))
