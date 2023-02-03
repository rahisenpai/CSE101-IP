n=int(input('enter: '))
l =[i for i in range(1,n+1) if i%3==0 or i%5==0 or i%7==0]
print(l)