# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
    q=int(n)%2
    if(q==0):
        p=str(n)
        s=int(p[-1])
        if(s==5):
            return int(n+1)
        elif(s==0):
            return int(n-1)
        elif(s<5 and s>0):
            return int(n+1)
        
        else:
            return int(n+1)
    else:
        return int(n)
        
	


