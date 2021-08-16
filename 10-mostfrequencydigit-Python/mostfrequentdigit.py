# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	p=[]
	l=[]
	n=str(n)
	x=0
	for i in range(len(n)):
		p.append(n[i])
	p=sorted(p)
	for j in range(len(p)):
		k=p.count(p[j])
		if(x<k):
			x=k
			l.append(p[j])
		elif(x>=k):
			pass
	
	a="".join(l) 
	b=a[-1]
	return int(b)
