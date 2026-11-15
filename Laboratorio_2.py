import numpy as np 
import matplotlib.pyplot as plt

def Rettnaif(n,h):
    sum=0
    for i in range(n): 
        sum+=np.exp(i*h)*h
    return sum

def Rett(n,h):
    sum=0
    for i in range(n): #uso formula derivata destra nb: il for va da 0 a n-1 con 0 incluso e n-1 escluso quindi arriva fino a n.
        sum+=np.exp((i+1/2)*h)*h
    return sum

def Trap(n,h):   
    sum=0
    for i in range(1,n-1): #uso formula derivata destra nb: il for va da 0 a n-1 con 0 incluso e n-1 escluso quindi arriva fino a n.
        sum+=0.5*(np.exp((i+1)*h)+np.exp(i*h))*h
    return sum

def Simpson(n,h):
    sum=0
    for i in range(1,n): 
            if i%2==1:
                sum += h*(np.exp((i-1)*h)/3 + 4*np.exp(i*h)/3 + np.exp((i+1)*h)/3)
    return sum

def main():
    x_max= 1
    n=[10,100,1000,10000,100000]
    h=[] 
    Rn=[] #vettore vuoto per il metodo dei rettangoli naif
    R=[] #vettore vuoto per il metodo dei rettangoli 
    T=[] #vettore vuoto per il metodo dei trapezi 
    S=[] #vettore vuoto per il metodo di Simpson 
    fa = np.exp(1) - 1  #valore esatto dell'integrale

    for i in range(len(n)):
        h.append(x_max/n[i])
        Rn.append(abs(Rettnaif(n[i],h[i])-fa))
        R.append(abs(Rett(n[i],h[i])-fa))
        T.append(abs(Trap(n[i],h[i])-fa))
        S.append(abs(Simpson(n[i],h[i])-fa))

    fig, ax = plt.subplots() #si definisce il grafico

    ax.semilogx () 
    ax.semilogy ()

    plt.rcParams.update({'font.size': 14})#si cambia il font
    ax.set_xlim(5,10**(5.3)) #si definiscono gli intervalli
    ax.set_ylim(10**(-16), 1) 

    ax.plot(n,Rn,  color='blue', label="Naif")#grafico
    ax.plot(n,R,  color='red', label="Rettangoli")#grafico
    ax.plot(n,T,  color='green', label="Trapezi")#grafico
    ax.plot(n,S,  color='pink', label="Simpson")#grafico

    
    ax.legend()
    ax.set_xlabel("X")
    ax.set_ylabel("f(X)")
    plt.show(block=True)


if __name__ == "__main__":
    main()
