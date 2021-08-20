# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.


# def noOfDigits(n):
# 	c=0
# 	while(n>0):
# 		n=n//10
# 		c+=1
# 	return c

# def isAutomorphicNumber(n):
#     nDigits=noOfDigits(n)
#     s=0
#     p=0
#     s=n**2
#     p=s%(10**nDigits)
#     print(p)
# n=890625
# print(isAutomorphicNumber(n))

def automorphic(n):
    #890625^2 = 793212890625
    a=n*n
    n=str(n)
    a=str(a)
    i=0
    while(i<=len(a)):
        q=a[i:]
        if(q==n):
            return True
        else:
            i+=1
    return False

def nthautomorphicnumbers(n):
    # Your code goes here
    c=1
    i=1
    while(c<n):
        if(automorphic(i)==True):
            c+=1
        i+=1
    return i-1
