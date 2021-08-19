def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
    
def isadditiveprime(n):
    c=0
    if(prime(n)==True):
        while(n>0):
            r=n%10
            c+=r
            n=n//10
        if(prime(c)==True):
            return True
    else:
        return False
n=23
print(isadditiveprime(n))