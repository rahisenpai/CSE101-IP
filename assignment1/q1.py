#funtion for unit place
def unit(x):
    if x==0:
        print('zero')
    elif x==1:
        print('one')
    elif x==2:
        print('two')
    elif x==3:
        print('three')
    elif x==4:
        print('four')
    elif x==5:
        print('five')
    elif x==6:
        print('six')
    elif x==7:
        print('seven')
    elif x==8:
        print('eight')
    elif x==9:
        print('nine')

#funtion for tens place except one
def tens(x):                
    if x==2:
        print('twenty', end=' ')
    elif x==3:
        print('thirty', end=' ')
    elif x==4:
        print('forty', end=' ')
    elif x==5:
        print('fifty', end=' ')
    elif x==6:
        print('sixty', end=' ')
    elif x==7:
        print('seventy', end=' ')
    elif x==8:
        print('eighty', end=' ')
    elif x==9:
        print('ninety', end=' ')

#function for one at tens place
def teens(x):
    if x==0:
        print('ten')
    elif x==1:
        print('eleven')
    elif x==2:
        print('twelve')
    elif x==3:
        print('thirteen')
    elif x==4:
        print('fourteen')
    elif x==5:
        print('fifteen')
    elif x==6:
        print('sixteen')
    elif x==7:
        print('seventeen')
    elif x==8:
        print('eighteen')
    elif x==9:
        print('nineteen')

num = int(input('enter (0,99): '))
#example in 23, pos1: 2, pos2: 3
pos2 = num%10
pos1 = num//10
#tens place is 0, single digit number
if pos1 == 0:
    unit(pos2)
#one at tens place
elif pos1 == 1:
    teens(pos2)
else:
    tens(pos1)
    #check unit place for 0
    if pos2 != 0:
        unit(pos2)