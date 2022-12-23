def fun(cost,allowance,r,month):
    sf=0.00
    balance=0
    while(balance<cost):
        sf += 0.01 #increment by 0.01 sf
        saving=allowance*sf
        balance=0
        for i in range(month):
            balance += saving
            #balance = balance*(1+r/12/100)**12
            balance = balance + balance*r/100
    return sf

cost = int(input('enter cost: '))
month = int(input('enter month: '))
sf = fun(cost,20000,0.5,month)
if sf>1.01:
    print('you cant purchase the laptop in the given time period even if you save total allowance')
else:
    print(sf)