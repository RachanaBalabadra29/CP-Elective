# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
# 27 = 3,3,3
# 94 = 2*47


import math

def func(n, p):
    c=0
    while((n%p)==0):
        c += 1
        n = n//p
    return c

# print(func(27,3))


def prime(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def primefactors(n):
    res = []
    for i in range(2, n+1):
        if prime(i) and n%i==0:
            res.append(i)
    return res

def sumOfDigits(n):
    res = 0
    while(n>0):
        res += n%10
        n //= 10
    return res

    # s=[]
    # for i in range(2,n + 1):
    #     if n % i == 0:
    #         count = 1
    #         for j in range(2,(i//2 + 1)):
    #             if(i % j == 0):
    #                 count = 0
    #                 break
    #         if(count == 1):
    #             s.append(i)
    # #print(s)
    # ans=0
    # for k in range(len(s)):
    #     ans+=s[k]
    # return ans

def checksmith(n):
    if prime(n): return False
    s = sumOfDigits(n)
    pfs = primefactors(n)
    res = 0
    for p in pfs:
        x = func(n,p)
        y = sumOfDigits(p)
        res += (x*y)
    return s==res

    # j=0
    # while(n>0):
    #     r=n%10
    #     j+=r
    #     n=n//10
    # a=primefactors(n)
    # if(j==a):
    #     return True
    # else:
    #     return False
def fun_nth_smithnumber(n):
    c=-1
    i=0
    while(c<=n):
        if(checksmith(i)==True):
            c+=1
        i+=1
    return i-1
# n=0
# print(fun_nth_smithnumber(n))
print(checksmith(204))
print(primefactors(204))
print(sumOfDigits(204))
print(func(204, 2)) # 204 = 2*102 = 2*2*51 = 2*2*3*17