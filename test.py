
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
dictden = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F',
    
}
answer = input('What is the number you want me to convert')
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
    
    print(  
    int(answer[0]) * 128 +
    int(answer[1]) * 64 +
    int(answer[2]) * 32 +
    int(answer[3]) * 16 +
    int(answer[4]) * 8 +
    int(answer[5]) * 4 +
    int(answer[6]) * 2 +
    int(answer[7]) * 1)
    
    
elif type == 'Denary' and contype == 'Hexadecimal':
    answer = int(answer)
    ans = math.floor(answer//16) 
    aps =answer%16
    print(str(ans)+str(dictden[aps]))
else:
	print('Please enter a valid number type')
