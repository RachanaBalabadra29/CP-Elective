# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).




def pronicnumber(n):
    for i in range(n):
        z=i*(i+1)
        if(n==z):
            return True
    return False

def nthpronicnumber(n):
	# Your code goes here
	if(n==0):
		return 0
	c=1
	i=0
	while(c<=n):
		if(pronicnumber(i)==True):
			c+=1
		i+=1
	return i-1