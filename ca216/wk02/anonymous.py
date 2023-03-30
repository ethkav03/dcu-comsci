from multiprocessing import *

for i in range(numProc):
    pi = Process(target=sayHi2, args=(name,))
    pi.start()