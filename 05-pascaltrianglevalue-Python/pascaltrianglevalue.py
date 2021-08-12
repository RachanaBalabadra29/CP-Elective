# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 

# 1
# 1 1
# 1 2 1
# 1 3 3 1


#
# from typing_extensions import ParamSpec


def fun_pascaltrianglevalue(row, col):
	if row<0:
		return 0
	if col<=0 or col>row:
		return 0
	pascal=[]
	for i in range(row+1):
		currRow=[]
		currRow.append(1)
		if i>=1:
			prevRow=pascal[i-1]
			for j in range(1,len(prevRow)):
				val=prevRow[j-1]+prevRow[j]
				currRow.append(val)
			currRow.append(1)
		pascal.append(currRow)
	return pascal[row][col]
	# arr = [[1]*(row+1)]*(row+1) # [[1,1,1,1,1,1],
	# 							#  [1,1,1,1,1,1],
	# 							#  [1,2,1,1,1,1],
	# 							#  [1,3,3,1,1,1],
	# 							#  [1,4,6,4,1,1],
	# 							#  [1,5,10,10,5,1]]
	# for i in range(2,row+1):
	# 	for j in range(1,i):
	# 		arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
	# return arr[row][col]