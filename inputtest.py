import msvcrt
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

fi = open('data.txt','a')

for i in range(10):
	#print('Press Any Key to dice! ')
	i = input('Press Any Key to dice! ')
	#i = msvcrt.getch()
	print(str(i))
	fi.write(i)
	fi.write('\n')

print("The total game loop is ",COUNTER)


close(fi)



