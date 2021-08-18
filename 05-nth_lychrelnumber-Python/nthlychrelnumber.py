# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


MAX_ITERATIONS = 50
def reverse(n):
    n=str(n)
    n=n[::-1]
    return int(n)

def isPalindrome(n):
  return n == reverse(n)
  
def isLychrel(n):
     
    for i in range(MAX_ITERATIONS):
        n = n + reverse(n)
         
        if (isPalindrome(n)):
            return False
     
    return True
# def lychrel(n):
#     q=0
#     i=1
#     while(q<=n):
#         c=n+reverse(n) #121
#         d=reverse(c)
#         if(c==d):
#             return True
#         else:
#             return False
#         c=c+reverse(c)
def nthlychrelnumbers(n):
    c=1
    i=1
    while(c<=n):
        if(isLychrel(i)==True):
            c+=1
        i+=1
    return i-1

#print(nthlychrelnumbers(n))