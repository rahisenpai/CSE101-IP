import math
def demand(price,a,b):
    _demand = int(math.e**(a-b*price))
    return _demand
    
def supply(price,c,d):
    _supply = int(math.e**(c+(d*price)))
    return _supply

price=1.0
count = 0
a,b,c,d = 10,1.05,1,1.06

if demand(price,a,b)<supply(price,c,d):
    print('no possible solutions')
else:
    for i in range(500):
        dem=demand(price,a,b)
        sup=supply(price,c,d)
        count +=1
        if dem>sup:
            price += price*0.05
        else:
            print('price where demand and supply cross:',price)
            print('number of items bought near equlibrium:',dem)
            print('number of items produced near equlibrium:',sup)
            break
if count == 500:
    print('solutions exist, but we couldnt find them')