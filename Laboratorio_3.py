import numpy as np 
import matplotlib.pyplot as plt

def f_gen(y,m,g,C):
    f=np.zeros(4)
    f[0]=y[2] #il vettore f in posizione 0 contiene il terzo elemento del vettore y
    f[1]=y[3] #il vettore f in posizione 1 contiene il quarto elemento del vettore y
    theta= np.atan2(y[3],y[2])
    f[2]=-0.5*1.22*0.47*np.pi*(0.05**2)*(f[0]**2 + f[1]**2)*np.cos(theta)/m
    f[3]=-0.5*1.22*0.47*np.pi*(0.05**2)*(f[0]**2 + f[1]**2)*np.sin(theta)/m-g
    return f


def main():
    v0=float(input('Scegli una velocità tra 100 e 200 m/s: '))
    theta0= np.pi/4
    y0=[0,0, v0*np.cos(theta0), v0*np.sin(theta0)] #coordinata generalizzata iniziale [posizione x, posizione y, velocita cos(tehta0), seno(theta0)]
    dt=0.001
    y1=np.zeros(4)
    m=2700*4*np.pi*pow(0.05,3)/3
    g=9.806
    C=0.47
    gitt=0

    found=False 
    while(not found):
        y1=y0+f_gen(y0,m,g,C)*dt
        if (y0[1]*y1[1]<0):
            gitt =y0[0]-(y1[0]-y0[0])/(y1[1]-y0[1])*y0[1]
            found=True 
        y0=y1
    d=2*pow(v0,2)*np.sin(theta0)*np.cos(theta0)/g
    print('Il risultato è: ' +str(gitt)+' m' )
    print('Il risultato è: ' +str(d)+' m' )

if __name__ == "__main__":
    main()
