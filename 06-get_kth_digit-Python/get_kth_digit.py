# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 

# (789,0,9), (789,1,8),
#     (789,2,7), (789,3,0),
#     (-789,0,9), (-780,4,0),
# ])

def fun_get_kth_digit(digit, k):
	digit=str(digit)
	if(k==0):
		p=digit[-1]
		return int(p)
	elif(k==1):
		p=digit[-2]
		return int(p)
	elif(k==2):
		p=digit[-3]
		return int(p)
	elif(k>=len(digit)):
		return 0

