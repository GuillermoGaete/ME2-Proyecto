import queue
import threading
import numpy
import time
import numpy as np
import matplotlib.pyplot as plt

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
while isRunning==True:
    point = q.get()
    if point == "Sali":
        isRunning=False
    else:
        plt.scatter(i,point)
        i=i+1
        plt.pause(0.00001)

print("sali")
plt.show()