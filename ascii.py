import msvcrt
import random

left = 20
x = 40 
y = 10
width = 81
height = 20

def printAvator(ch,x1):
	printchar(left,1,'*',0)
	printchar(x1-1,1,ch,0)
	printchar(width-x1-2,1,'*',1)


def printchar(scount,ccount,char,nl):
		
	for i in range(scount):		
		print(' ',end='')

	for j in range(ccount):	

		if nl==1:
			print(char)
		else:
			print(char,end='')		


printchar(left,width,'*',0)
print('\n')


for ydwon in range(20-y):
	printchar(left,1,'*',0)
	printchar(79,1,'*',1)

printAvator('A',x)
printAvator('G',x+3)
printAvator('B',x-6)





