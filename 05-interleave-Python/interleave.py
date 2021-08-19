# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
    i=0
    j=0
    c=""
    if(len(s1)==len(s2)):
        while(i<len(s1)):
            c+=s1[i]+s2[j]
            i+=1
            j+=1
        return c
    elif(len(s1)<len(s2)):
        x=len(s2)-len(s1)
        r=s2[len(s1):]
        s2=s2[:len(s1)]
        while(i<len(s1)):
            c+=s1[i]+s2[j]
            i+=1
            j+=1
        return c+r
    elif(len(s1)>len(s2)):
        r=s1[len(s2):] 
        s1=s1[:len(s2)]
        while(i<len(s1)):
            c+=s1[i]+s2[j]
            i+=1
            j+=1
        return c+r