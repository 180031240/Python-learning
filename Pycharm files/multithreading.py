#Thread - A light weight process. When we breakdown a big process into small parts, each part is called as a thread.
#By default every excution has one thread which is called as main thread.
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()

sleep(0.2)
t2.start()

#Here, join() will say to main thread that when the t1 and t2 threads finish then print bye. It's like, t1 has gone to do it's task and t2 has
#gone to do it's task. So, once they join together -- once they come back, then print bye
t1.join()
t2.join()
print("Bye")