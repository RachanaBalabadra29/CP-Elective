# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 

# def recursion_binarysearchvalues(L, v):
# 	# Your codes goes here
# 	low=0
# 	high=len(L)-1
# 	p=[]
# 	while(low<=high):
# 		mid=(low+high)//2
# 		if(L[mid]<v):
# 			p.append((mid,L[mid]))
# 			low=mid+1
# 		elif(L[mid]>v):
# 			p.append((mid,L[mid]))
# 			high=mid-1
# 		else:
# 			p.append((mid,L[mid]))
# 			return p
# 	return p



def binary_search(L, low, high, v,p=[]):
    if high >= low:
        mid = (high + low) // 2
        if L[mid] == v:
            p.append((mid,L[mid]))
            return p
        elif L[mid] > v:
            p.append((mid,L[mid]))
            return binary_search(L, low, mid - 1, v, p)
        else:
            p.append((mid,L[mid]))
            return binary_search(L, mid + 1, high, v, p)
    else:
        return p
        
        
def recursion_binarysearchvalues(L,v):
    # your code goes here
	A = []
	binary_search(L, 0, len(L)-1, v, A)
	return A


L = ['a', 'c', 'f', 'g', 'm', 'q']
v = 'z'
print(recursion_binarysearchvalues(L,'a'))
print(recursion_binarysearchvalues(L,'c'))
print(recursion_binarysearchvalues(L,'f'))
print(recursion_binarysearchvalues(L,'g'))
print(recursion_binarysearchvalues(L,'m'))
print(recursion_binarysearchvalues(L,'q'))
print(recursion_binarysearchvalues(L,'z'))
print(recursion_binarysearchvalues(L,'b'))