#GALE SHAPELY ---> Stable Matching

max=500
mMark={}
wc={}
mc={}
women={}
men={}
for i in range(max):
    women[i]={}
    men[i]={}
    mMark[i]={}
    wc[i]={}
    mc[i]={}
def wPrefersMoverM1(w,m,m1,n):
    for i in range(1,n+1):
        if(women[w][i]==m):         ##Check in the woman 'w' preference list women[][];
            return 1               ## If it is 'm' return true else if it is 'm1' return false.
        elif(women[w][i]==m1):
            return 0
def stablemarriage(n):
    freecount=n
    for i in range(1,max):
        mMark[i]=0
        wc[i]=-1
    while freecount>0:
        for m in range(1,n+1):
            for i in range(1,n+1)  :
                if mMark[m]==0 :
                    w=men[m][i]
                    if wc[w]==-1:
                        wc[w]=m
                        mMark[m]=1
                        freecount=freecount-1
                    else:
                        m1=wc[w]
                        if wPrefersMoverM1(w,m,m1,n):
                            wc[w]=m
                            mMark[m]=1
                            mMark[m1]=0
n=int(input('\n Enter the number of men and women :'))
print('\n Enter the womens prefernce list :')
for i in range(1,n+1):
    print('\n Women {0} :'.format(i))
    for j in range(1,n+1):
        women[i][j]=int(input())
print('\n Enter the mens prefernce list :')
for i in range(1,n+1):
    print('\n men {0} :'.format(i))
    for j in range(1,n+1):
        men[i][j]=int(input())
stablemarriage(n)
for i in range(1,n+1):
    mc[wc[i]]=i
for i in range(1,n+1):
    print('{0} man is paired with {1} women \n '.format(i,mc[i]))
