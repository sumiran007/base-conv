
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
dictbinhex = {
	'0000':'0',
	'0001':'1',
	'0010':'2',
	'0011':'3',
	'0100':'4',
 	'0101':'5',
	'0110':'6',
	'0111':'7',
	'1000':'8',
	'1001':'9',
	'1010':'A',
	'1011':'B',
	'1100':'C',
	'1101':'D',
	'1110':'E',
	'1111':'F',
}
hexbin = {
	'0':'0000',
	'1':'0001',
	'2':'0010',
	'3':'0011',
	'4':'0100',
	'5':'0101',
	'6':'0110',
	'7':'0111',
	'8':'1000',
	'9':'1001',
	'A':'1010',
	'B':'1011',
 	'C':'1100',
	'D':'1101',
	'E':'1110',
	'F':'1111',
 
}
answer = input('What is the number you want me to convert')
type = input('What is the type of number you want me to convert from Hexadecimal, Binary or Denary')
contype = input('What is the type of number you want me to convert to, Hexadecimal, Binary or Denary')
if type == 'Hexadecimal' and contype == 'Binary':
    bin = dicthex[answer[0]]*16
elif type == 'Binary' and contype == 'Hexadecimal':
    nib1 = answer[0:4]
    nib2 = answer[4:8]
    nib3 = answer[8:12]
    nib4 = answer[12:16]
    nib = dictbinhex[nib1] + dictbinhex[nib2] + dictbinhex[nib3] + dictbinhex[nib4]
    print(nib)
elif type == 'Hexadecimal' and contype == 'Denary':
    hexden = dicthex[answer[0]]*16 + dicthex[answer[1]*1]
    print((hexden))
elif type == 'Denary' and contype == 'Binary':
    hi = int(answer)
    varden = math.floor(hi/128)
elif type == 'Binary' and contype == 'Denary':
    
    print(  
    int(answer[0]) * 32768 +
    int(answer[1]) * 16384 +
    int(answer[2]) * 8192 +
    int(answer[3]) * 4096 +
    int(answer[4]) * 2048 +
    int(answer[5]) * 1024 +
    int(answer[6]) * 512 +
    int(answer[7]) * 256 +
    int(answer[8]) * 128 +
    int(answer[9]) * 64 +
    int(answer[10]) * 32 +
    int(answer[11]) * 16 +
    int(answer[12]) * 8 +
    int(answer[13]) * 4 +
    int(answer[14]) * 2 +
    int(answer[15]) * 1)
    
    
elif type == 'Denary' and contype == 'Hexadecimal':
    answer = int(answer)
    anl = math.floor(answer/4096)
    anp = math.floor(answer/256)
    ans = math.floor(answer//16) 
    aps =answer%16
    print(str(dictden[anl])+str(dictden[anp])+str(dictden[ans])+str(dictden[aps]))
else:
	print('Please enter a valid number type')
