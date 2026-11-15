import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f( y, m1, m2, g, l1, l2):
    f=np.zeros(4)
    f[0]=y[2] 
    f[1]=y[3]
    f[2]=-(1/(l1*(m1+m2*(1-(np.cos(y[0]-y[1])**2)))))*(m2*l2*(np.sin(y[0]-y[1]))*(y[3]**2)+g*(m1+m2)*np.sin(y[0])-(np.cos(y[0]-y[1]))*(-m2*l1*(np.sin(y[0]-y[1]))*(y[2]**2)+m2*g*np.sin(y[1])))
    f[3]=-(1/(l2*((m2-(m2**2/(m1+m2))*(np.cos(y[0]-y[1]))**2))))*((-m2/(m1+m2))*(np.cos(y[0]-y[1]))*(m2*l2*(np.sin(y[0]-y[1]))*(y[3])**2+g*(m1+m2)*(np.sin(y[0])))-m2*l1*(np.sin(y[0]-y[1]))*(y[2])**2+m2*g*(np.sin(y[1])))
    return f

def runge( y, m1, m2, g, l1, l2, dt):
    Y1= y
    Y2= y + f(Y1, m1, m2, g, l1, l2)*dt/2
    Y3= y + f(Y2, m1, m2, g, l1, l2)*dt/2
    Y4= y + f(Y3, m1, m2, g, l1, l2)*dt
    Yf= y + ( f(Y1, m1, m2, g, l1, l2) + 2*f(Y2, m1, m2, g, l1, l2) + 2*f(Y3, m1, m2, g, l1, l2) + f(Y4, m1, m2, g, l1, l2))*dt/6
    return Yf

def animazione(dt,t,coord, trail_length=500):
    fig, ax = plt.subplots()
    l1x=np.zeros((2),dtype=np.float64)
    l1y=np.zeros((2),dtype=np.float64)
    history2x = np.zeros(( trail_length))
    history2y = np.zeros(( trail_length))
    history3x = np.zeros(( trail_length))
    history3y = np.zeros(( trail_length))
    
    l1x[0]=0
    l1y[0]=0
    l1x[1]=coord[0,0]
    l1y[1]=coord[1,0]
    line1 = ax.plot(l1x,l1y)[0]
    l2x=np.zeros((2),dtype=np.float64)
    l2y=np.zeros((2),dtype=np.float64)
    l2x[0]=coord[0,0]
    l2y[0]=coord[1,0]
    l2x[1]=coord[2,0]
    l2y[1]=coord[3,0]
    line2 = ax.plot(l2x,l2y)[0]

    # Traiettorie
    trail2 = ax.plot(history2x, history2y, 'b-', alpha=0.5)[0]
    trail3 = ax.plot(history3x, history3y, 'g-', alpha=0.5)[0]
    # Dischi
    disc1, = ax.plot([], [], 'ro', markersize=10)  # Disco rosso per il primo punto
    disc2, = ax.plot([], [], 'bo', markersize=10)  # Disco blu per il secondo punto
    disc3, = ax.plot([], [], 'go', markersize=10)  # Disco verde per il terzo punto

    
    ax.set(xlim=[-4, 4], ylim=[-4, 4], xlabel='X [m]', ylabel='Y [m]')
    ax.legend('Label')


    def update(frame):
        l1x[0]=0
        l1y[0]=0
        l1x[1]=coord[0,frame]
        l1y[1]=coord[1,frame]
        l2x[0]=coord[0,frame]
        l2y[0]=coord[1,frame]
        l2x[1]=coord[2,frame]
        l2y[1]=coord[3,frame]
        line1.set_xdata(l1x)
        line1.set_ydata(l1y)
        line2.set_xdata(l2x)
        line2.set_ydata(l2y)
         # Aggiorna i dischi
        origine=np.zeros((2,1))
        disc1.set_data(origine)  # Origine (0,0)
        origine[0,0]=coord[0,frame]
        origine[1,0]=coord[1,frame]
        disc2.set_data(origine)  # Secondo punto
        origine[0,0]=coord[2,frame]
        origine[1,0]=coord[3,frame]
        disc3.set_data(origine)  # Terzo punto
        
        # Aggiorna le traiettorie
        history2x = np.zeros(( trail_length))
        history2y = np.zeros(( trail_length))
        history3x = np.zeros(( trail_length))
        history3y = np.zeros(( trail_length))
        frame_in=max(frame-trail_length,0)
        for ifr in range(frame-frame_in):
            history2x[ifr]=coord[0,ifr+frame_in]
            history2y[ifr]=coord[1,ifr+frame_in]
            history3x[ifr]=coord[2,ifr+frame_in]
            history3y[ifr]=coord[3,ifr+frame_in]
        
        
        trail2.set_data(history2x, history2y)
        trail3.set_data(history3x, history3y)
        
        return line1, line2, disc1, disc2, disc3, trail2, trail3


    ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=int(dt*1000), blit=True)
    plt.show()

def main ():
    m1=float(input('Inserire la massa del pendolo 1 (1): '))
    m2=float(input('Inserire la massa del pendolo 2 (1): '))
    l1=float(input('Inserire la lunghezza del pendolo 1 (1): '))
    l2=float(input('Inserire la lunghezza del pendolo 2 (1): '))
    theta01=float(input('Inserire theta1 (179): '))
    theta02=float(input('Inserire theta2 (179): '))
    theta1 = np.pi/180*theta01
    theta2 = np.pi/180*theta02
    v1=float(input('Inserire la velocità del pendolo 1 (0): '))
    v2=float(input('Inserire la velocità del pendolo 2 (0): '))
    dt=0.001 #tempo
    N=10000 #numero di passi
    n=1000
    g=9.81

    y=[theta1, theta2, v1, v2] #stato iniziale
    #E=[]
    coord=np.zeros((4,n))
    j=0

    for i in range(N+1):
        y1=runge(y, m1, m2, g, l1, l2, dt)
        if(i%10==1):
            coord[0,j]=l1*np.sin(y1[0])
            coord[1,j]=-l1*np.cos(y1[0])
            coord[2,j]=coord[0,j]+l2*np.sin(y1[1])
            coord[3,j]=coord[1,j]-l2*np.cos(y1[1])
            j=j+1
            #E.append(-(m1+m2)*g*l1*np.cos(y1[0])-m2*g*l2*np.cos(y1[1])+0.5*m1*(l1**2)*(y1[2]**2)+0.5*m2*((l1**2)*(y1[2]**2)+(l2**2)*(y1[3]**2))+m2*l1*l2*np.cos(y1[0]-y1[1])*y1[2]*y1[3])
        y=y1

    tempo=[]
    for i in range(N+1):
        tempo.append(i*dt)

    ani=animazione(dt, tempo, coord)

    '''fig, ax = plt.subplots() #grafico
    ax.plot(tempo, E, color='pink', label='Energia')
    plt.rcParams.update({'font.size': 14})#cambiamo il font
    ax.set_xlim(0, tempo[-1])  # Definiamo gli intervalli
    ax.set_ylim(0, max(E) + 1)
    
    ax.legend()
    ax.set_xlabel("t")
    ax.set_ylabel("E")
    plt.show(block=True)'''

if __name__ == "__main__":
    main()
