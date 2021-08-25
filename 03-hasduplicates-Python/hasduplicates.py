# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.




def hasduplicates(L):
    c=0
    p=[]
    for i in range(len(L)):
        for j in range(len(L[i])):
            p.append(L[i][j])
    #print(p)
    
    s=[]
    for i in p:
        if i not in s:
            s.append(i)
            
    if(s==p):
        return False
    else:
        return True

