import numpy as np
import random

def f(x,y,z):
    return 3*x**2+y**2+2*z**2

step=0.005

def integrate(f,rx,ry,rz):
    area=0.0
    for x in np.arange(rx[0],rx[1],step):
        for y in np.arange(ry[0],ry[1],step):
            for z in np.arange(rz[0],rz[1],step):
                area+=f(x,y,z)*step**3
    return area

print(integrate(f,[0,1],[0,1],[0,1]))

upper=6
lower=0

def mcintegrate(f,rx,ry,rz,n=100000):
    hits=0
    for _ in range(n):
        x=random.uniform(rx[0],rx[1])
        y=random.uniform(ry[0],ry[1])
        z=random.uniform(rz[0],rz[1])
        p=random.uniform(lower,upper)
        if f(x,y,z)>p:
            hits+=1
    return (rx[1]-rx[0])*(ry[1]-ry[0])*(rz[1]-rz[0])*(upper-lower)*(hits/n)

print(mcintegrate(f,[0,1],[0,1],[0,1]))