import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def main():
    lato=float(input("Impostare il lato cella di simulazione (1m):\t"))
    n=int(input("Impostare i punti per lato (100):\t"))
    lun=float(input("Impostare la lunghezza delle piastre (0.7m):\t"))
    larg=float(input("Impostare la larghezza delle piastre (0.1m):\t"))
    d=float(input("Impostare la distanza delle piastre (0.5m):\t"))
    pot1=float(input("Impostare il potenziale della piastra 1 (100V):\t"))
    pot2=float(input("Impostare il potenziale della piastra 2 (-100V):\t"))
    potb=float(input("Inserire il potenziale di bordo (0V):\t"))
    e0=8.8542*10**(-12)

    h=lato/(n-1)

    m=np.zeros((n,n,n,n),dtype=np.float64)
    f=np.zeros((n,n),dtype=np.float64)
    charge=np.zeros((n,n),dtype=np.float64)

    

    nx01 = int((lato / 2 - d / 2 - larg) * n / lato)
    nx11 = int((lato / 2 - d / 2) * n / lato)
    nx02 = int((lato / 2 + d / 2) * n / lato)
    nx12 = int((lato / 2 + d / 2 + larg) * n / lato)
    ny0 = int(((lato - lun) / 2) * n / lato)
    ny1 = int((lun + (lato - lun) / 2) * n / lato)
    hx=larg/(nx11-nx01-1)
    hy=lun/(ny1-ny0-1)

    print(f"Piastre da {nx01}-{nx11} e {nx02}-{nx12} con altezza {ny0}-{ny1}")
    print(f"hx {hx} hy {hy}")

    
    #formattazione della matrice M grazie a np 
    for i in range(0,n-1):
        for j in range(0,n-1):
            if not (nx01 <= i <= nx11 and ny0 <= j <= ny1) and not (nx02 <= i <= nx12 and ny0 <= j <= ny1):
                m[i,j,i,j]=-2.0*2/h**2  

                m[i,j,i+1,j]=1.0/h**2
                m[i,j,i-1,j]=1.0/h**2
                m[i,j,i,j+1]=1.0/h**2
                m[i,j,i,j-1]=1.0/h**2
    
    #condizioni di dirichlet
    for i in range(n):
            m[0,i,0,i]=1.0
            m[i,0,i,0]=1.0
            m[n-1,i,n-1,i]=1.0
            m[i,n-1,i,n-1]=1.0
    
    vb=0
    
    for i in range(n):
            f[0,i]=vb
            f[i,0]=vb
            f[n-1,i]=vb
            f[i,n-1]=vb

    for i in range(nx01,nx11+1):
        for j in range(ny0,ny1+1):
            f[i,j]=100
            m[i,j,i,j]=1.0
            

    for i in range(nx02,nx12+1):
        for j in range(ny0,ny1+1):
            f[i,j]=-100
            m[i,j,i,j]=1.0


    m=m.reshape((n**2,n**2))  
    f=f.reshape((n**2))  
    phi=np.linalg.solve(m,f)
    phi=phi.reshape(n,n)
    
    charge=np.zeros((n,n), dtype=np.float64)
    for i in range (1,n-1):
        for j in range (1, n-1):
             charge[i,j]=-(1/e0)*((phi[i+1,j]-2*phi[i,j]+phi[i-1,j])/h**2+(phi[i,j+1]-2*phi[i,j]+phi[i,j-1])/h**2)

    X=np.zeros((n,n),dtype=np.float64)
    Y=np.zeros((n,n),dtype=np.float64)
    for i in range(n):
         for j in range(n):
              X[i,j]=h*i
              Y[i,j]=h*j
              
    f=f.reshape(n,n)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, f, vmin=f.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

    plt.show()

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, charge, vmin=charge.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

    plt.show()

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, phi, vmin=phi.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

    plt.show()
    
if __name__ == "__main__":
    main()