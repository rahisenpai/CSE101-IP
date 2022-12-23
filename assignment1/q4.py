import math

def velocity(t):
    return (2000* math.log(140000/(140000-2100*t)) - 9.8*t)

def integrate(end, start, dt):
    dist = 0
    t = start
    while (t+dt) <= end:
        #vel = velocity(t)
        avgvel = (velocity(t) + velocity((t+dt)))/2
        dist += (avgvel*dt)
        t += dt
    return dist

a = int(input('start time: '))
b = int(input('end time: '))
distance = integrate(b, a, 0.25)
print('distance travelled: ',distance)