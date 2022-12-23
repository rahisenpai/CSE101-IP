def fact(x):
    ans=1
    for i in range(1,x+1):
        ans *= i
    return ans

def sin(x):
    value=0
    for i in range(50):
        value += ((-1)**i)*(x**(2*i+1))/fact(2*i+1)
    return value

def cos(x):
    value=0
    for i in range(50):
        value += ((-1)**i)*(x**(2*i))/fact(2*i)
    return value

angle = int(input('angle in degrees(0-90): '))
base = int(input('base: '))
rad = angle*3.14/180
hypotenuse = base/cos(rad)
height = hypotenuse*sin(rad)
print('height of the pole is',height,'m')
print('distance to tip of pole is',hypotenuse,'m')