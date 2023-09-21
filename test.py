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
type = input('What is the type of number you want me to convert from Hexadecimal, Binary or Denary, type H, B or D to enter. ')
contype = input('What is the type of number you want me to convert to, Hexadecimal, Binary or Denary, type H, B or D to enter. ')
type = type.lower()
contype = contype.lower()
if type == 'h' and contype == 'b':
    bin = hexbin[answer[0]]+hexbin[answer[1]]+hexbin[answer[2]]+hexbin[answer[3]]
    print(bin)
elif type == 'b' and contype == 'h':
    nib1 = answer[0:4]
    nib2 = answer[4:8]
    nib3 = answer[8:12]
    nib4 = answer[12:16]
    nib = dictbinhex[nib1] + dictbinhex[nib2] + dictbinhex[nib3] + dictbinhex[nib4]
    print(nib)
elif type == 'h' and contype == 'd':
    hexden = dicthex[answer[0]]*4096 + dicthex[answer[1]*256] + dicthex[answer[2]]*16 + dicthex[answer[3]]
    print((hexden))
elif type == 'd' and contype == 'b':
    answer = int(answer)
    varden = str(answer//32768)+ str((answer%32768)//16384) + str((answer%16384)//8192) + str((answer%8192)//4096) + str((answer%4096)//2048) + str((answer%2048)//1024) + str((answer%1024)//512) + str((answer%512)//256) + str((answer%256)//128) + str((answer%128)//64) + str((answer%64)//32) + str((answer%32)//16) + str((answer%16)//8) + str((answer%8)//4) + str((answer%4)//2) + str((answer%2)//1)
    print(varden)
elif type == 'b' and contype == 'd':
    
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
    
    
elif type == 'd' and contype == 'h':
    answer = int(answer)
    anl = math.floor(answer/4096)
    anp = math.floor(answer/256)
    ans = math.floor(answer//16) 
    aps =answer%16
    print(str(dictden[anl])+str(dictden[anp])+str(dictden[ans])+str(dictden[aps]))
else:
	print('Please enter a valid number type')
 
