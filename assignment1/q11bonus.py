#given two numbers show their prime factorisation,lcm, hcf and if they are armstrong numbers print so

def prime(n):
    x=n
    for i in range(2,n+1):
        if x%i == 0:
            while(x%i == 0):
                print(i,end='x')
                x=x/i
    print('1')
        
def lcm(a,b):
    max = a if a>b else b
    while(1):
        if max%a == 0 and max%b == 0:
            return max
        max+=1

def hcf(a,b):
    min = a if a<b else b
    while(1):
        if a%min == 0 and b%min == 0:
            return min
        min-=1

def armstrong(num):
    sum = 0
    a=num
    while(a!=0):
        x = a%10
        sum += x**3
        a=a//10
    if sum == num:
        return True
    else:
        return False

a = int(input('enter 1st number: '))
b = int(input('enter 2nd number: '))

print('prime factorisation of',a,'is',end=' ')
prime(a)
print('prime factorisation of',b,'is',end=' ')
prime(b)

m = lcm(a,b)
f = hcf(a,b)
print('lcm of',a,'and',b,'is',m)
print('hcf of',a,'and',b,'is',f)

a1=armstrong(a)
a2=armstrong(b)
if a1:
    print(a,'is an armstrong number')
if a2:
    print(b,'is an armstrong number')