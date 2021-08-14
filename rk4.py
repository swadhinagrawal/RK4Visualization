import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace


def dfdx(x,t):
    return 4*x*t

def inte(t):
    return np.exp(2*(t**2))


t = 0
dt = 0.3
t1 = 0
dt1 = 0.01
f0 = 1
fx = [f0]
tm = [t]
tm1 = [t1]
f = f0
intfx = [f0]
count = 0
fig = plt.figure()



plt.ion()
while t<10:
    x = linspace(0,1,100)
    f1 = f
    while t1<t:
        t1 += dt1
        tm1.append(t1)
        f1 = inte(t1)
        intfx.append(f1)
    plt.plot(tm1,intfx,c='purple')
    k1 = dfdx(f,t)
    c1 = plt.plot(x+t,f+k1*x,c='blue')
    s1 = plt.scatter(t,f,c='blue')

    # plt.pause(0.1)
    k2 = dfdx(f+dt*k1/2,t+dt/2)
    c2 = plt.plot(x+t+dt/2,f+dt*k1/2+k2*x,c='green')
    s2 = plt.scatter(t+dt/2,f+dt*k1/2,c='green')

    # plt.pause(0.1)
    k3 = dfdx(f+dt*k2/2,t+dt/2)
    c3 = plt.plot(x+t+dt,f+dt*k1/2+ dt*k2/2+k3*x,c='black')
    s3 = plt.scatter(t+dt,f+dt*k1/2+dt*k2/2,c='black')

    # plt.pause(0.1)
    k4 = dfdx(f+dt*k3,t+dt)
    c4 = plt.plot(x+t+3*dt/2,f+dt*k1/2+ dt*k2/2+ dt*k3/2+k4*x,c='brown')
    s4 = plt.scatter(t+3*dt/2,f+dt*k1/2+dt*k2/2+dt*k3/2,c='brown')

    # plt.pause(0.1)
    f += dt*(k1+2*k2+2*k3+k4)/6
    t += dt
    
    fx.append(f)
    tm.append(t)
    plt.plot(tm,fx,color = 'red')
    
    plt.pause(1)
    c1.pop(0).remove()
    s1.remove()
    c2.pop(0).remove()
    s2.remove()
    c3.pop(0).remove()
    s3.remove()
    c4.pop(0).remove()
    s4.remove()
    plt.show()
