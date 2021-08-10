# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

# (468, 0, 1, 461), (468, 1, 1, 418),
#     (468, 2, 1, 168), (468, 3, 1, 1468),
#     (-468, 3, 1, -1468)

def fun_set_kth_digit(n, k, d):
    if(n<0):
        n=abs(n)
        a=str(-d)+str(n)
        return int(a)
    n=str(n)
    d=str(d)
    n=n[::-1]
    if(k<len(n)):
        p=n.replace(n[k],d)
        p=p[::-1]
        return int(p)
    elif(k>len(n)-1):
        d+=n[::-1]
        
    return int(d)


