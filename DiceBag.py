import random

def D20(qty):
	""" Returns a list of size qty filled with random numbers (20 sided) """
	return ROLLGEN(qty, 20)

def D10(qty):
	""" Returns a list of size qty filled with random numbers (10 sided) """
	return ROLLGEN(qty, 10)
	
def D8(qty):
	""" Returns a list of size qty filled with random numbers (8 sided) """
	return ROLLGEN(qty, 8)
	
def D6(qty):
	""" Returns a list of size qty filled with random numbers (6 sided) """
	return ROLLGEN(qty, 6)
	
def D4(qty):
	""" Returns a list of size qty filled with random numbers (4 sided) """
	return ROLLGEN(qty, 4)
	
def D2(qty):
	""" Returns a list of size qty filled with random numbers (2 sided) """
	return ROLLGEN(qty, 2)

def ROLLGEN(qty, size):
	""" Does the random generation of dice, returns in list """
	x = 0
	Numlist = []
	while x < qty:
		randnum = random.randint(1, size)
		x = x + 1
		Numlist.append(randnum)
	return Numlist