def value(x,a=1,b=-10.5,c=34.5,d=-35):
    return a*x**3 + b*x**2 + c*x + d

def differntial(x,a=1,b=-10.5,c=34.5):
    return 3*a*x**2 + 2*b*x + c

def root(x0):
    count=0
    for i in range(100):
        z = value(x0)
        if z<=0.2 or z>=-0.2:
            x1 = x0 - z/differntial(x0)
            x0=x1
            count+=1
        else:
            slope=differntial(x0)
            x0 = z/slope +x0
    if count==0:
        print('no roots found')
    else:
        print(x1)

a,b,c,d = 1,-10.5,34.5,-35
x0=float(input('enter x0: '))
print('value of polynomial for x is',value(x0))
root(x0)