# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

#([[2, 7, 6], [9, 5, 1], [4, 3, 8]], True),

#([[2, 7, 6]
#  [9, 5, 1]
#  [4, 3, 8]])

def ismostlymagicsquare(a):
	# Your code goes here
    add=0
    k=[]
    for i in a:
        for j in range(len(i)):
            add+=i[j]
        k.append(add)
        add=0
    #return k
    q=[]
    h=0
    w=0
    d=0
    while(d<len(a[0])):
        for i in range(0,len(a)):
            res=a[i][w]
            h+=res
            #w+=1
        w+=1
        d+=1
        q.append(h)
        h=0
    #print(q)
    l=0
    m=len(a)-1
    diagonal1=0
    diagonal2=0
    for i in a:
        ans=i[l]
        diagonal1+=ans
        l+=1
        
        ans1=i[m]
        diagonal2+=ans1
        m-=1
    if(diagonal1==diagonal2  and k==q):
        return True
    else:
        return False