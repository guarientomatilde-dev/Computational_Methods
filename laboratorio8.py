import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
import matplotlib.animation as animation

def animazione(dt,n_punti,n_frames,x, psi):
    #psi: array (n_punti,n_frames)
    #x: array(n_punti)

    fig, ax = plt.subplots()
    

    # Traiettorie
    line = ax.plot(x, psi[:,0], 'b-', alpha=0.5)[0]
    

    


    ax.set(ylim=[0,np.max(psi)])
    

    def update(frame):
        line.set_ydata(psi[:,frame])

        
        return line, line


    ani = animation.FuncAnimation(fig=fig, func=update, frames=n_frames, interval=int(dt*10),blit=True)
    plt.show()



def main():
    L=500
    x0=200
    m=1
    q=2
    Nx=1000

    sigma=20
    a=250
    b=260
    V0=1.7
    deltat=0.1
    Ntimestep=2000
    n=Nx-2
    h=L/(n-1)
    ai=int(a*n/L)
    bi=int(b*n/L)

    v=np.zeros((n),dtype=np.float64) 
    d=np.zeros((n),dtype=complex)  
    m=np.zeros((3,n),dtype=complex)  
    upper_diag = np.ones(n - 1, dtype=np.complex128)  #Diagonale superiore
    phit0=np.zeros((n), dtype = complex)
    phi=np.zeros((n,Ntimestep), dtype = complex)
    phif=np.zeros((n, Ntimestep), dtype=float)
    F= np.zeros((n), dtype=np.complex128)
    prob = np.zeros(Ntimestep, dtype=np.float64)


    for i in range(ai, bi): 
        v[i]=V0
    
    #print (v)

    im=1.0j
    for i in range (0,n):
        phit0[i] = np.exp(q * (h * i) * 1j) * np.exp(-(h * i - x0)*2 / (2 * sigma*2))
   

    sca = np.vdot(phit0, phit0)
    phit0 = phit0 / np.sqrt(sca) #rendo normalizzato la funzione phi
    

    #costruisco la matrice M 
    for i in range( n):
        if a <= h * i <= b:
            d[i] = (4*im*m*h**2/deltat - 2 - 2*m*h**2*v[i])

    m[0,1:n]=1.0
    m[2,0:n-1]=1.0
    m[1,0:n]=d[0,n]
    upper_diag[:]=1.0 

    for k in range(1,Ntimestep):            
        for i in range(n):
            if(i==0):
                F[i] = - phit0[i+1] + 2*phit0[i] - phit0[i-1] + (4*(h**2/deltat)*1j)*phit0[i] + (2*m*h**2)*v[i]*phit0[i]
            else:
                F[i] = - phit0[i+1] + 2*phit0[i] - phit0[i-1] + (4*(h**2/deltat)*1j)*phit0[i]
        
        '''phit0[0,k] = 0
        phit0[n,k] = 0
        phi = solve_banded((1,1), elemento_M,F)'''
        
        
        phi = solve_banded((1,1), m, F)
        sca = np.vdot(phi, phi)
        phif [0:n,k]=np.conj(phit0[0,n])*phit0[0:n]
        print('Il modulo quadrato è:', sca )
        phit0=phif
    
    
    animazione(deltat, Nx, Ntimestep, phif)
    
if __name__ == "__main__":
    main()