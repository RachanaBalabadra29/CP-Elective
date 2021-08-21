# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
    # Your code goes here
    c=0
    p=[]
    if k==2:
        for i in range(len(L)):
            if(i==len(L)-1):
                p.append(L[i])
                break
            if k==2:
                c+=1
                if(L[i]==L[i+1]):
                    c+=1
                    if(c==k):
                        pass
                elif(L[i]!=L[i+1]):
                    p.append(L[i])
        return p
    elif k==3:
        for i in range(len(L)):
            if(i==k):
                p.extend(L[i:])
                break
            if(L[i]==L[i+1]==L[i+2]):
                pass
            else:
                p.append(L[i])
        return p