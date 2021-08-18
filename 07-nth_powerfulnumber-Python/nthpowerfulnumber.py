# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def isPowerfulNumber(n):
	while(n%2== 0):
		num=0
		while(n%2==0):
			n=n//2
			num=num+1
		if(num==1):
			return False
	for i in range(3, int(n**0.5)+1,2):
		num=0
		while(n%i==0):
			n=n//i
			num=num+1
		if(num==1):
			return False
	return (n==1)

#use helper function
def nthpowerfulnumber(n):
	if(n==0):
		return 1
	c=0
	i=1
	while(c <=n):
		if(isPowerfulNumber(i)==True):
			c+=1
		i=i+1
	return i-1


