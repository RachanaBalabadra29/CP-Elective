# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


def squaresum(n):
    # your code goes here
    d=0
    while(n>0):
        r=n%10
        c=r*r
        d+=c
        n=n//10
    return d

def happynum(n):
    s=n
    f=n
    while True:
        s=squaresum(s)
        f=squaresum(squaresum(f))
        if(s!=f):
            continue
        else:
            break
    if(s==1):
        return True
    else:
        return False

def nth_happy_number(n):
	c=1
	i=-2
	while(c<=n):
		if(happynum(i)==True):
			c+=1
		i+=1
	return i-1
