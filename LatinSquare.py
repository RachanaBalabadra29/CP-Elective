# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    p=[]
    for i in lst:
        for j in range(len(i)):
            c=i.count(i[j])
            p.append(c)
    for i in p:
        if(i!=1):
            return False
    return True
      

lst=[[1,2,3],
     [2,3,1],
     [3,1,2]]

print(isLatinSquare(lst))