import time
import threading

def fun1():
    print('one')
    print(time.ctime())
    time.sleep(1)
def fun2():
    print('two')
    print(time.ctime())
#fun1()
#fun2()
# both are running sequentally bcoz of gli in python need to break to make it run parrley/cocuttrntly both are diff
#multi threading
#creating threads
t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
#starting the threads
t1.start()
t2.start()

#passing argument while threading
def func1(name):
    print(name)
    print(time.ctime())
def func2(name):
    print(name)
    print(time.ctime())
t1=threading.Thread(target=func1,args=('subhash',)) # the parameter should be either a list or tuple
t2=threading.Thread(target=func2,args=('vaibhac',))
t1.start()
t2.start()   #start and join produce same o/p but in start() threaads are not close before the child threads
t1.join()    # use join to close sub threads  and then closes parent threads
t2.join()
#If we use join
# it closes the python thread first then closes the thread running inside the program
# closes the func1,func2 first and then closes python.main thread
# if we dont use  join()
#it closes the python thread first may be the innner threads running and this to absurd suring system crash so need to use join instead of start

# hititng the same function using 2 threads to do some operaaton it wont affect
print("----------------------")
def func1(name,delay):
    counter=0
    while(counter<5):
        print(name)
        print(time.ctime())
        time.sleep(delay)
        counter+=1
t1=threading.Thread(target=func1,args=('dhoni',2))
t2=threading.Thread(target=func1,args=('kolhi',4))
t1.start()
t2.start()
t1.join()
t2.join()
print("----------------------")