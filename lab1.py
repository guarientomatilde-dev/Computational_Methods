import numpy as np 
import matplotlib.pyplot as plt


def Ordineh(f,h): 
    n=len(f) 
    der=np.zeros(len(f)) 
    for i in range(0,n-1): 
        der[i]=(f[i+1]-f[i])/h
    return der


def Ordineh2(f,h): 
    n=len(f) 
    der=np.zeros(len(f)) 
    for i in range(1,n-1):  
        der[i]=(f[i+1]-f[i-1])/(2*h)
    return der


def Ordineh4(f,h): 
    n=len(f) 
    der=np.zeros(len(f)) 
    for i in range(2,n-2): 
        der[i]=(-f[i+2]+8*f[i+1]-8*f[i-1]+f[i-2])/(12*h)
    return der

def main():
    x_max=float(input('Dammi X massimo :'))
    n=int(input('Dammi n :'))
   

    x=[]#crea una lista per ora vuota
    f=[]
    fa=[]

    h=x_max/n 


    for i in range(n):
        x.append(x_max/n*i)
        f.append(np.sin(x[i]))
        fa.append(np.cos(x[i])) 
       

    foh=Ordineh(f,h) 
   

    Errh=foh-fa 
    
    foh2=Ordineh2(f,h)

    Errh2=foh2-fa

    foh4=Ordineh4(f,h)

    Errh4=foh4-fa

    fig, ax = plt.subplots()#definiamo un grafico

    plt.rcParams.update({'font.size': 14})#cambiamo il font
    ax.set_xlim(x[2],x[n-3])#definiamo gli intervalli
    ax.set_ylim(np.min(Errh[4:n-5]),np.max(Errh[4:n-5])) 

    plt.plot(x,Errh,  ls='-', label="O(h)")#grafico
    plt.plot(x,Errh2,  ls='-', label="O(h^2)")#grafico
    plt.plot(x,Errh4,  ls='-', label="O(h^4)")#grafico
   
    
    ax.legend()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.show(block=True)




if __name__ == "__main__":
    main()
