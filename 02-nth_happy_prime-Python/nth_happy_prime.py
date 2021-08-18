# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True


def square(n):
    sqnum=0
    while(n):
        sqnum += (n%10)*(n%10)
        n=n//10
    return sqnum

def happy(n):
    s=n
    f=n
    while True:
        s=square(s)
        f=square(square(f))
        if(s!=f):
           continue
        else:
           break
    if(s==1):
        return True
    else:
        return False

def happyprime(n):
    if(not prime(n)):
        return False
    return happy(n)
    
def fun_nth_happy_prime(n):
    c=-2
    i=0
    while(c<n):
        if(happyprime(i)==True and prime(i)==True):
            c+=1
        i+=1
    return i-1