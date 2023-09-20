import pygame
import math
#pygame.init()
#window_size = (800, 800)
dicthex = {
	'0':0,
	'1':1,
	'2':2,
	'3':3,
	'4':4,
	'5':5,
	'6':6,	
	'7':7,
	'8':8,
	'9':9,
	'A':10,
	'B':11,
	'C':12,
	'D':13,
	'E':14,
	'F':15,
}
answer = input('Whta is the number you want me to convert')
type = input('What is the type of number you want me to convert from Hexadecimal, Binary or Denary')
contype = input('What is the type of number you want me to convert to, Hexadecimal, Binary or Denary')
if type == 'Hexadecimal' and contype == 'Binary':
    bin = type[0]*16
elif type == 'Binary' and contype == 'Hexadecimal':
    print((answer))
elif type == 'Hexadecimal' and contype == 'Denary':
    hexden = dicthex[answer[0]]*16 + dicthex[answer[1]*1]
    print((hexden))
elif type == 'Denary' and contype == 'Binary':
    
	print((answer))	
elif type == 'Binary' and contype == 'Denary':
	print((answer))
elif type == 'Denary' and contype == 'Hexadecimal':
    answer = int(answer)
    ans = math.floor(answer//16) 
    aps =answer%16
    print(str(ans)+str(dicthex[aps]))
else:
	print('Please enter a valid number type')
