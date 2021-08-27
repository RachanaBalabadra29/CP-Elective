# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.



def pro(n):
    f=[]
    a=[]
    res=n**5
    # print(res)
    while(res>0):
        s=res%10
        f.append(s)
        res=res//10
    for i in range(10):
        a.append(i)
        if i not in f:
           return False
    return True
# n=309
# print(pro(n))

def nthwithproperty309(n):
    i=1
    c=0
    while(c<=n):
        if(pro(i)==True):
            c+=1
        i+=1
    return i-1




