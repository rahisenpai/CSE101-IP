def fun(cost,allowance,sf,r):
    saving=allowance*sf
    balance=0
    month=0
    while(balance<cost):
        balance += saving
        balance = balance*(1+r/12/100)**12
        #balance = balance + balance*r/100
        month += 1
    return month,(balance-cost)

cost = int(input('enter cost: '))
month,left = fun(cost,20000,0.1,0.5)
print('months:',month)
print('balance left:',left)