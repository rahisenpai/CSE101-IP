x0,y0 = 5,5
distance = 0
while(1):
    d = int(input('enter distance: '))
    if d<=0:
        break
    elif d<=25:
        y0 += d
    elif d<=50:
        y0 -= d
    elif d<=75:
        x0 += d
    else:
        x0 -= d
    distance += d
print('final coordinates are (',x0,',',y0,')',sep='')
print('total distance traveled is',distance)
print('straight line distance is',(x0*x0 + y0*y0)**0.5)