#funtion for unit place
def unit(x):
    if x==0:
        print('zero',end=' ')
    elif x==1:
        print('one',end=' ')
    elif x==2:
        print('two',end=' ')
    elif x==3:
        print('three',end=' ')
    elif x==4:
        print('four',end=' ')
    elif x==5:
        print('five',end=' ')
    elif x==6:
        print('six',end=' ')
    elif x==7:
        print('seven',end=' ')
    elif x==8:
        print('eight',end=' ')
    elif x==9:
        print('nine',end=' ')

#funtion for tens place except one
def tens(x):                
    if x==2:
        print('twenty',end=' ')
    elif x==3:
        print('thirty',end=' ')
    elif x==4:
        print('forty',end=' ')
    elif x==5:
        print('fifty',end=' ')
    elif x==6:
        print('sixty',end=' ')
    elif x==7:
        print('seventy',end=' ')
    elif x==8:
        print('eighty',end=' ')
    elif x==9:
        print('ninety',end=' ')

#function for one at tens place
def teens(x):
    if x==0:
        print('ten',end=' ')
    elif x==1:
        print('eleven',end=' ')
    elif x==2:
        print('twelve',end=' ')
    elif x==3:
        print('thirteen',end=' ')
    elif x==4:
        print('fourteen',end=' ')
    elif x==5:
        print('fifteen',end=' ')
    elif x==6:
        print('sixteen',end=' ')
    elif x==7:
        print('seventeen',end=' ')
    elif x==8:
        print('eighteen',end=' ')
    elif x==9:
        print('nineteen',end=' ')

def fun(num):
    if num == 0:
        return False
    #example in 23, pos2: 2, pos1: 3
    else:
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
        return True

n = int(input('enter (less than 100crore): '))
c = n//10**7
l = (n-c*10**7)//10**5
t = (n-c*10**7-l*10**5)//10**3
h = (n-c*10**7-l*10**5-t*10**3)//10**2
rest = n-c*10**7-l*10**5-t*10**3-h*100
if fun(c):
    print('crore',end=' ')
if fun(l):
    print('lakh',end=' ')
if fun(t):
    print('thousand',end=' ')
if fun(h):
    print('hundred',end=' ')
fun(rest)