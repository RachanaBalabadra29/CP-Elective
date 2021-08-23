# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.



def findeven(n,count,result):
	if n==0:
		return result
	else:
		r=n%10
		if r%2==0:
			result+=r*10**count
			count+=1
		n=n//10
		return findeven(n,count,result)
def even(i,l):
	if i==len(l):
		return l
	else:
		l[i]=findeven(l[i],0,0)
		i+=1
		return even(i,l)						


def fun_recursion_onlyevendigits(l):
	i=0
	res=even(i,l)
	return res


# def fun_recursion_onlyevendigits(l): 
# 		return []