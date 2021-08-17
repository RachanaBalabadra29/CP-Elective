# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!


def fabricyards(inches):
	# Your code goes here...
	if(inches==0):
		return 0
	elif(inches<=36):
		return 1
	elif(inches<=72):
		return 2
	elif(inches>72):
		return 3

def fabricexcess(inches):
	# Your code goes here...
	if(inches==0):
		return 0
	elif(inches<=36):
		a=36
		c=abs(a-inches)
		return c
	elif(inches<=72):
		b=72
		d=abs(b-inches)
		return d
	elif(inches>72):
		e=108
		f=abs(e-inches)
		return f