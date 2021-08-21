# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.






def fixmostlymagicsquare(L):
    # Your code goes here
    add=0
    k=[]
    for i in L:
        for j in range(len(i)):
            add+=i[j]
        k.append(add)
        print(k)
        add=0
    #return k
    q=[]
    h=0
    w=0
    d=0
    while(d<len(L[0])):
        for i in range(0,len(L)):
            res=L[i][w]
            h+=res
            #w+=1
        w+=1
        d+=1
        q.append(h)
        h=0
    #print(q)
    l=0
    m=len(L)-1
    diagonal1=0
    diagonal2=0
    for i in L:
        ans=i[l]
        diagonal1+=ans
        l+=1
        
        ans1=i[m]
        diagonal2+=ans1
        m-=1
        
    
    same=[]
    for i in k:
        if k.count(i)==1:
            uniquevalue=i
            indx=k.index(i)
        if k.count(i)>1:
            same.append(i)
            
    same1=[]
    for i in q:
        if q.count(i)==1:
            uniquevalue1=i
            indx1=q.index(i)
        if q.count(i)>1:
            same1.append(i)
            
    if(uniquevalue==uniquevalue1 and same[0]==same1[0]):
        changevalue=uniquevalue-same[0]
        
    p=L[indx][indx1]
    z=p-changevalue
    L[indx][indx1]=z
    
    return L
        
    # if(diagonal1==diagonal2  and k==q):
    #     return True
    # else:
    #     return False
        
# a=[[2, 7, 9], [9, 5, 1], [4, 3, 8]]
# print(ismostlymagicsquare(a))