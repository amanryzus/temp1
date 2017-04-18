import random
import time
def quicksort(a):
    less,higher,equal=[],[],[]
    if len(a)>1:
        pivot=a[0]
        for x in a:
            if x<pivot:
                less.append(x)
            if x==pivot:
                equal.append(x)
            if x>pivot:
                higher.append(x)
        return quicksort(less)+equal+quicksort(higher)
    else:
        return a
a=[random.randint(0,100) for i in range(int(input('\n Enter the size of array : ')))]
print(a)
start=time.clock()
print(quicksort(a))
print('%f'%(time.clock()-start))
