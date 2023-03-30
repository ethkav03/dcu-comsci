from multiprocessing import *

def sayHi2(n):
    print("Hi", n, "from process", current_process().pid)

def manyGreetings():
    print("Hi from process", current_process().pid, "(main process)")
    
    name = "Jimmy"
    p1 = Process(target=sayHi2, args=(name,))
    p2 = Process(target=sayHi2, args=(name,))
    p3 = Process(target=sayHi2, args=(name,))

    p1.start()
    p2.start()
    p3.start()

def manyGreetings2():
    name = input("Enter your name: ")
    numProc = input("How many processes? ")

    for i in range(int(numProc)):
        Process(target=sayHi2, args=(name,)).start()

#execute
manyGreetings2()

p = Process(target=sayHi2, args=(name,))
p.start()