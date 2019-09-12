import random

loc = 0
HOME = 100

S1H = 98
S1T = 22

S2H = 76
S2T = 62

L1S = 5
L1E = 75

L2S = 24
L2E = 38

COUNTER = 0


while 1:
	#print('Press Any Key to dice! ')
	input('Press Any Key to dice! ')
	r = random.randrange(1,7)
	loc = loc + r

	if loc == S1H:
		print('Ohh... big snake!!')
		loc = S1T
	elif loc == S2H:
		print('Ohh... snake!!')
		loc = S2T
	elif loc == L1S:
		print('Wow... Yayyy big ladder!!')
		loc = L1E
	elif loc == L2S:
		print('Wow... Yayyy ladder!!')
		loc = L2E
	elif loc > HOME:
		print('Ekkk')
		loc = HOME - ( loc - HOME ) 	
	elif loc == HOME:
		print('Wow... I WON')
		break;
	print('\nNew Location is ',loc)
	COUNTER = COUNTER +1

print("The total game loop is ",COUNTER)





