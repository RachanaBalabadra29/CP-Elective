# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = ((x1 - x2) * (x1 - x2)) + \
		((y1 - y2) * (y1 - y2))
	b = ((x1 - x3) * (x1 - x3)) + \
        ((y1 - y3) * (y1 - y3))
	c = ((x2 - x3) * (x2 - x3)) + \
        ((y2 - y3) * (y2 - y3))
	if ((a == (b + c) and a != 0 and b != 0 and c != 0) or
        (b == (a + c) and a != 0 and b != 0 and c != 0) or
        (c == (a + b) and a != 0 and b != 0 and c != 0)):
		return True
	else:
		return False
