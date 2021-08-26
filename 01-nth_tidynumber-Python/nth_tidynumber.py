# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46



def noOfDigits(n):
	c=0
	while(n>0):
		n=n//10
		c+=1
	return c

def isTidyNumber(n):
    r=0
    s=n%10
    c=0
    nDigits=noOfDigits(n)
    for i in range(nDigits):
        r=n%10
        n=n//10
        if(r<=s):
            c+=1
        s=r
    if(c==nDigits):
        return True
    else:
        return False

def fun_nth_tidynumber(n):
    i=0
    c=-1
    while(c<=n):
        if(isTidyNumber(i)==True):
            c+=1
        i+=1
    return(i-1)

