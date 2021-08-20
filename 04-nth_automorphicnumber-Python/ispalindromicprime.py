def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def palindrome(n):
    p=0
    s=n
    while(n>0):
        r=n%10
        p=p*10+r
        n=n//10
    if(p==s):
        return True
    else:
        return False

def isPalindromicPrime(n):
    if(prime(n)==True and palindrome(n)==True):
        return True
    else:
        return False

# n=2
# print(isPalindromicPrime(n))

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")