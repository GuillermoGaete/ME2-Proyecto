import queue
import threading
import numpy
import time
import numpy as np
import matplotlib.pyplot as plt
NUM_PUNTOS=128
isRunning = True
def medidor(q):
    x5_data=np.load("../medidas/estrutcura_viernes_128_X1.npy")
    for x in range(len(x5_data)):



        q.put(x5_data[x])


        time.sleep(0.1)
    q.put("Sali")

q = queue.Queue(maxsize=20)
worker = threading.Thread(target=medidor, args=(q,))
worker.start()
i=0
db=[]
print("Generando grafico polar de las mediciones tomadas")
r = np.arange(-0.75, 0.25, 1/NUM_PUNTOS)
theta = 2*np.pi*r
ax = plt.subplot(111, projection='polar')
ax.set_rlabel_position(0)  # Move radial labels away from plotted line
ax.grid(True)
ax.set_rmax(-30)
ax.set_rticks([-60,-50,-40,-30])  # Less radial ticks
ax.set_title("Radiation lobule of a patch antenna", va='bottom')
    
#print(np.floor((max(db)+10)/10))

while isRunning==True:
    
    
    
    point = q.get()
    
    if point == "Sali":
        isRunning=False
    else:
        
        #plt.clf()
        db.append(point)
        print(float(theta[i:i+1]), db[i])
        #exit()
        ax.plot(theta[:i+1], db)
    

        i=i+1
        plt.pause(0.05)
        #plt.draw()


       
    
    
    
    



    
print("sali")
plt.show(block=True)
