# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



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

def fun_nearestkaprekarnumber(n):
    h=[]
    for i in range(0,20):
        ans=fun_nth_kaprekarnumber(i)
        h.append(ans)
    # for j in range(len(h)):
    result = lambda h : abs(h - n)
    nearest = min(h, key=result)   
    return nearest
    
        
# n=52
# print(fun_nearestkaprekarnumber(n))