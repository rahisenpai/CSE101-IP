def profit(m):
    P,x1,x2 = 0,0,0
    #a max of 50 tables can be made in a day
    for i in range(0,51):
        #a max of 120 chairs can be made in a day
        for j in range(0,121):
            if ((8*i+2*j)<=400) and ((2*i+1*j)<=120):
                if i>m:
                    profit = 90*m + 100*(i-m) + 25*m + 30*(j-m)
                else:
                    profit = 90*i + 25*j
                if profit>P:
                    P = profit
                    x1,x2 = i,j
    print("tabels:",x1,'\t chairs:',x2,'\t max profit:',P)

M = int(input('margin: '))
profit(M)