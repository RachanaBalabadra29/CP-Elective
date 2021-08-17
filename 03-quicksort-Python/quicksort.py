"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array,start,end):
	# Your code goes here
	if(end-start)>1:
		p=partition(array,start,end)
		quicksort(array,start,p)
		quicksort(array,p+1,end)

def partition(array,start,end):
	pivot=array[start]
	i=start+1
	j=end-1
	while True:
		while(i<=j and array[i]<=pivot):
			i+=1
		while(i<=j and array[j]>=pivot):
			j-=1
		if(i<=j):
			array[i],array[j]=array[j],array[i]
		else:
			array[start],array[j]=array[j],array[start]
			return j
array=input()
start=0
end=len(array)
quicksort(array,start,end)
print(array)
