# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def isPrime(n):
	if(n<2):
		return False
	for i in range(2,n):
		if(n%i==0):
			return False
	return True


def noOfDigits(n):
	c=0
	while(n>0):
		n=n//10
		c+=1
	return c

def rotate(n):
	nDigits=noOfDigits(n)
	r=n%10
	n=n//10
	return r*(10**(nDigits-1)) + n

def isZeroPresent(n):
	while(n>0):
		r=n%10
		if(r==0):
			return True
		n=n//10
	return False		

def isCircularPrime(n):
	if(isZeroPresent(n)==True):
		return False
	nDigits=noOfDigits(n)
	for i in range(nDigits):
		n=rotate(n)
		if(isPrime(n) == False):
			return False
	return True	

def nthcircularprime(n):
	i=0
	c=0
	while(c<=n):
		if(isCircularPrime(i)==True):
			c+=1
		i+=1
	return(i-1)	


