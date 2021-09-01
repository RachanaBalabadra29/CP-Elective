# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

# [("name",45),("name2",50)]

def topScorer(data):
    # Your code goes here...
    if data=="": return None
    res = []
    p = data.split("\n")
    for el in p:
        if el=="": continue
        x = el.split(",")
        score = 0
        for i in range(1,len(x)):
            score += int(x[i])
        res.append((x[0],score))
    res.sort(key = lambda x : x[1], reverse=True)
    highest = []
    highScore = res[0][1]
    for el in res:
        if el[1] == highScore:
            highest.append(el[0])
    if len(highest)==1:
        return highest[0]
    else:
        s = ""
        for player in highest:
            s += (player + ",")
        return s[:-1]

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
p = data.split("\n")
print(p)

assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
