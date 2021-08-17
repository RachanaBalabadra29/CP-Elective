# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	
	p=[]
	s=s.replace(" ","")
	if(len(s)==1):
		return s
	for i in range(len(s)):
		p.append(s[i])
	d=[]
	for j in p:
		c=p.count(j)
		if(c>1):
			d.append((j,c))
			a=set(d)
	b=list(a)
	b.sort(key=lambda x:x[1],reverse=True) 
	#print(b)
	for i in range(len(b)):
		v=(b[n-1])
	return(v[0])


