# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def kaprekar(n):
    c=str(n)
    a=n*n #2025 #81
    i=0
    digits=""
    res1=0
    res3=0
    while(i<len(c)):
        r=a%10 #1
        i+=1
        digits+=str(r) #1
        a=a//10 #8
    res=a+int(digits[::-1]) #81
    k=a
    j=k%10
    
    u=a
    l=u%10
    u=u//10
    l1=u%10
    if(l==0 and l1==0):
        u=u//10
        res3=u+int(digits[::-1])
    if(j==0):
        k=k//10
        res1=k+int(digits[::-1])
    if(n==res or n==res1 or n==res3):
        return True
    else:
        return False

def fun_nth_kaprekarnumber(n):
    c=0
    i=1
    while(c<=n):
        if(kaprekar(i)==True):
            c+=1
        i+=1
    return i-1