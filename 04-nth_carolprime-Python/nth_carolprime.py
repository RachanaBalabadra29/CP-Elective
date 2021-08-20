# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).


def prime(p):
    if (p < 2):
        return False
    for i in range(2,p):
        if (p % i == 0):
            return False
    return True


# def carolprime(n):
#     h=int((2**n - 1)**2 - 2)
#     if(prime(h)==True):
#         # print(h)
#         return True
#     else:
#         return False


def fun_nth_carolprime(n):
    r=0
    p=1
    result=0
    while(r<=n):
        result=((2**p - 1)**2 - 2)
        if prime(result):
               r+=1
        p+=1
    return result
