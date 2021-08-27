# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
# maxDigit = 3
# maxDigitCount = 2
# digit = -1
# digitCount = 0
# 11777
# 7
# 1
def longestdigitrun(n):
	# Your code goes here
	n = abs(n)
	maxDigit = -1
	maxDigitCount = 0
	currDigit = -1
	currDigitCount = 0
	while(n>0):
		# print(n)
		# print(maxDigit, currDigit)
		# print("-----")
		if n%10 == currDigit:
			currDigitCount += 1
		else:
			if maxDigitCount<currDigitCount:
				maxDigit = currDigit
				maxDigitCount = currDigitCount
			elif maxDigitCount==currDigitCount:
				if currDigit < maxDigit:
					maxDigit = currDigit
			currDigit = n%10 # 1
			currDigitCount = 1
		n //= 10
	if currDigitCount==maxDigitCount and currDigit<maxDigit:
		maxDigit = currDigit
	return maxDigit

print(longestdigitrun(12345))