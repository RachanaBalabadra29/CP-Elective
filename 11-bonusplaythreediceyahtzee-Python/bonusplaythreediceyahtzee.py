# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the 
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2 
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the 
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use 
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some 
# helper functions that do part of the work, and then those helper functions will make our final 
# function much easier to write. 

# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will 
# be represented by the integer 432. With that, let's start writing some code. Be sure to write 
# your functions in the same order as given here, since later functions will make use of earlier 
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns 
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice 
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it 
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by 
# calling score, which you already wrote). The function should return two values -- the resulting hand 
# and the score for that hand. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))


def bonusplaythreediceyahtzee(dice):
	# Your code goes here
	hand1=dice%1000
	dice1=dice//1000
	h1,d1=playstep2(hand1,dice1)
	h2,d2=playstep2(h1,d1)
	s=checkscore(h2)
	return h2,s
	


def handtodice(hand):
    # your code goes here
    x=[]
    p=len(str(hand))
    m=0
    i=1
    while(i<=p):
        m=hand%10
        x.append(m)
        i+=1
        hand=hand//10
    c=(x[::-1])
    return c

def handtodice(hand):
    # your code goes here
    x=[]
    p=len(str(hand))
    m=0
    i=1
    while(i<=p):
        m=hand%10
        x.append(m)
        i+=1
        hand=hand//10
    c=(x[::-1])
    return c

# def playstep2(hand,dice):
#     # your code goes here
#     a=handtodice(hand)
#     b=handtodice(dice)
#     c=[]
#     y=[]
#     for i in range(len(a)):
#         count=a.count(a[0])
#         count2=a.count(a[1])
#         if(count==1 and count2>1):
#            c.append(a[i])
#     for i in range(1,len(a)):
#         count1=a.count(a[i])
#         if(count1==1):
#             a[i]=b[-1]
#             b.pop()
#         elif(count1>1):
#             a[0]=b[-1]
#             b.pop()
#             break
#     w=(sorted(a,reverse=True))
#     e="".join(str(x) for x in w)
#     f="".join(str(x) for x in b)   
#     # print(e)
#     # print(f)
    
#     y=tuple((e,f)) 
#     r=[]
#     for el in y:
#         r.append(int(el))
#     # v=(544, 23)
#     # print(type(v))
#     return tuple(r)


def playstep2(hand,dice):
	a,b,c=handtodice(hand)
	dice1=dice
	if(a==b and b==c and c==a):
		return(hand,dice)
	if(a!=b and b!=c and c!=a):
		h1=a
		h2=dice1%10
		dice1=dice1//10
		h3=dice1%10
		dice1=dice1//10
		h=dicetoorderedhand(h1,h2,h3)
		return(h,dice1)
	if(b==c):
		h2=b
		h3=c
		h1=dice%10
		dice=dice//10
		h=dicetoorderedhand(h1,h2,h3)
		return(h,dice)


def dicetoorderedhand(a, b, c):
	# your code goes here
	x=""
	x+=str(a)
	x+=str(b)
	x+=str(c)
	y="".join(sorted(x,reverse=True))
	return int(y)

def checkscore(hand):
	a,b,c=handtodice(hand)
	arr=[]
	score=0
	arr.append(a)
	arr.append(b)
	arr.append(c)
	arr.sort()
	if(a!=b and b!=c and c!=a):
		score=arr[2]
	elif((a==b and b!=c) or (b==c and c!=a)):
		score=10+b+b
	elif(a==b and b==c):
		score=20+a+a+a
	return score
