def value(x):
    ans=0
    for i in range(len(coeff)):
        ans += coeff[i]*x**(n-i)
    return ans

def differntial(x):
    ans=0
    for i in range(len(coeff)-1):
        ans += (n-i)*coeff[i]*x**(n-i-1)
    return ans

'''def root(n,start,end):
    count,list =0,[]
    x0 = start
    while(x0 <= end):
        for i in range(75):
            z = value(x0)
            if z<=0.2 or z>=-0.2:
                x1 = x0 - z/differntial(x0)
                x0 = x1
            else:
                slope=differntial(x0)
                x0 = z/slope +x0
        y = round(x1,1)
        if y not in list:
            list.append(y)
            print(list[count],end=' ')
            count+=1
        x0 += 1'''

def root(n,start,end):
    count,list = 0,[]
    for x0 in range(start,end):
        for i in range(75):
            z = value(x0)
            if z<=0.2 or z>=-0.2:
                x1 = x0 - z/differntial(x0)
                x0 = x1
            else:
                slope=differntial(x0)
                x0 = z/slope +x0
        y = round(x1,1)
        if y not in list:
            list.append(y)
            print(list[count],end=' ')
            count += 1
            
n = int(input('enter number of roots: '))
coeff = [float(num) for num in input('enter space separated coefficients: ').split()]
x1=int(input('enter x1: '))
x2=int(input('enter x2: '))
root(n,x1,x2)