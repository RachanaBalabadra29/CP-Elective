# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

# no.of cols in m1 = no. of rows in m2
# [[2,4,5],     [[2,4,9,8],
#  [3,5,7]]      [4,6,3,6],
#                [4,4,2,4]

# no.of rows in m1 x no.of cols in m2
# 2*2 + 4*4 + 5*4
# m1[0][0]*m2[0][0] + m1[0][1] + m2[1][0] + m1[0][2] + m2[2][0]

rows = 3
cols = 4
x = [[0]*cols]*rows
y = [[0 for i in range(cols)] for j in range(rows)]

print(x)
print(y)

def fun_matrixmultiply(m1, m2):
    if len(m1[0]) != len(m2):
        return None
    rows = len(m1)
    cols = len(m2[0])
    # res = [[0]*cols]*rows
    res = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(len(m1)):    # i = 0,1
        for j in range(len(m2[0])):     # j = 0,1,2,3
            # m1[i][k]
            # m2[k][j]
            for k in range(len(m2)):    # k = 0,1,2
                res[i][j] += m1[i][k] * m2[k][j]
    return res




