import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

def main():
    ry2eV=13.605*2
    a=float(input("Inserire la largezza della buca (Bohr):\t"))
    n=int(input("Inserire il numero di punti della griglia:\t"))
    gamma=int(input("Inserire il valore di gamma (1,2,5 Bohr):\t"))
    l=int(input("Inserire il numero quantico (0,1,2...):\t"))
    h=a/(n-1)
    v=np.zeros((n),dtype=np.float64) 
    vk=int(input("Tipo di Potenziale: 1 buca infinita 2 buca Coulombiano 3 buca di Yukawa\t"))
    if(vk==1):
        v[:]=0. #metto valori tutti uguali per ogni elemento
    elif(vk==2):
        for i in range(1,n):
            v[i]=-1/(i*h) # uso . per rendere il numero float e non intero
    elif(vk==3):
        for i in range(1,n):
            v[i]=-(1/(i*h))*np.exp(-i*h/gamma) # uso . per rendere il numero float e non intero
 
    d=np.zeros((n-1),dtype=np.float64)  
    u=np.zeros((n-2),dtype=np.float64)  #termini di matrice (in questo caso L=U perche il coefficiente b è nullo)
    
    '''#popoliamo la matrice m con cicli for 
    for i in range(0,n-2):
        d[i]=(-2.0*(-0.5)/h**2+v[i+1]+ 0.5*l*(l+1)/((i+1)*h)**2)
    for i in range(0,n-3):
        u[i,i+1]=(-0.5)/h**2
        u[i+1,i]=(-0.5)/h**2'''

    for i in range(0, n - 1):
        d[i] = (-2.0 * (-0.5) / h**2 + v[i + 1] + 0.5 * l * (l + 1) / ((i + 1) * h)**2)

    for i in range(0, n - 2):
        u[i] = (-0.5) / h**2  # termini sopra e sotto diagonali

    e, w = eigh_tridiagonal(d,u) #calcolo gli autovalori 'e' e gli autovettori 'w'

    M = np.zeros((n - 1, n - 1), dtype=np.float64)

    # Diagonale principale
    for i in range(n - 1):
        M[i, i] = d[i]

    # Termini sopra e sotto diagonale
    for i in range(n - 2):
        M[i, i + 1] = u[i]
        M[i + 1, i] = u[i]

    # Imposta i primi e ultimi valori della diagonale a 1
    M[0, 0] = 1  # Primo elemento
    M[n - 2, n - 2] = 1  # Ultimo elemento

    # Visualizza la matrice tridiagonale
    print("Matrice tridiagonale:")
    print(M)
    for i in range(n-2):
        print("Energia calcolata (eV):\t"+str(e[i]*ry2eV ),"\t e quella di una buca piatta (ev):\t"+str(np.pi**2/(2*a**2)*(i+1)**2*ry2eV))

    nump=int(input("Numeri di auto-funzioni da stampare"))
    
    #creiamo il grafico delle parti radiali degli autostati
    fig, ax = plt.subplots()
    lx=np.zeros((n,nump),dtype=np.float64)
    ly=np.zeros((n,nump),dtype=np.float64)
    for i in range(n):
        lx[i,:]=i*h
    ly[0,:]=0
    ly[n-1,:]=0
    #ly[j + 1, ip] = w[j, ip] ** 2
    line=[]
    for ip in range(nump):
        for j in range(n-2):
            ly[j+1]=w[j,ip]**2
       
        plt.plot(lx[:,ip],ly[:,ip])
   
    ax.set( xlabel='X [Bohr]')
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
