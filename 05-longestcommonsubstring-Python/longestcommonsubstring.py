# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"
# ab, bc, cA, AB, BC
# res = "AB"

def getAllSubstrings(s, n):
    # abcdsdsf = 7
    # 4
    # abcd,  bcds,  cdsd,  dsds,  sdsf
    # [0..3] [1..4] [2..5] [3..6] [4..7]
    # for i in range(4):
    #   s[i:i+n]
    res = []
    if n>len(s): return res
    for i in range(len(s)-n+1):
        res.append(s[i:i+n])
    return res

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    n = len(s1)
    m = len(s2)
    x = min(n,m)
    if x==n:
        l = n
        res = "z"
        found = False
        while(l>0):
            sub = getAllSubstrings(s1, l) # abc, bcd, cde, def
            for substr in sub:
                if substr in s2 and substr < res:
                    res = substr
                    found = True
            if found: return res
            l -= 1
        return ""
    else:
        l = m
        res = "z"
        found = False
        while(l>0):
            sub = getAllSubstrings(s2, l)
            for substr in sub:
                if substr in s1 and substr < res:
                    res = substr
                    found = True
            if found: return res
            l -= 1
        return ""

print(longestcommonsubstring("abcABC", "zzabZZAB"))
print(longestcommonsubstring("abcdef", "abqrcdest"))
print("cde"<"abqrcdest")