def fun1(x):
    if x<=1:
        return 1
    print('* '*(x)+2*(n-x)*'  '+'* '*(x))
    fun1(x-1)

def fun2(x):
    if x<=0:
        return 1
    print('* '*(n-x+1)+2*(x-1)*'  '+'* '*(n-x+1))
    fun2(x-1)
 
n=int(input('enter n: '))
'''for i in range(n):
    print('* '*(n-i)+2*i*'  '+'* '*(n-i))
for j in range(2,n+1):
    print('* '*j+2*(n-j)*'  '+'* '*j)'''
fun1(n)
fun2(n)