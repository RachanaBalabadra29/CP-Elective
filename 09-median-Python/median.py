# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	
	low=0
	high=len(a)
	mid=(low+high)//2

	if(len(a)==0):
		return None

	if(len(a)%2==0):
		mid=(low+high)//2
		res=(a[mid-1]+a[mid])/2
		return res
	else:
		return a[mid]