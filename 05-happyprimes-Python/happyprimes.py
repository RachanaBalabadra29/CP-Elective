# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!


def squaresum(n):
    # your code goes here
    d=0
    while(n>0):
        r=n%10
        c=r*r
        d+=c
        n=n//10
    return d

def ishappynumber(n):
    s=n
    f=n
    while True:
        s=squaresum(s)
        f=squaresum(squaresum(f))
        if(s!=f):
            continue
        else:
            break
    if(s==1):
        return True
    else:
        return False


def prime(n):
    if n<2: return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

    
def ishappyprimenumber(n):
    # Your code goes here
    x=prime(n)
    y=ishappynumber(n)
    if(x==True and y==True):
        return True
    else:
        return False