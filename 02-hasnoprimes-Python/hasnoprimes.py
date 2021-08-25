# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.





def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def fun_hasnoprimes(l):
    c=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if(prime(l[i][j])==True):
                c+=1
    if(c==0):
        return True
    else:
        return False

