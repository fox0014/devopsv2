import threading
import time

class MyThread(threading.Thread):
        def __init__(self,my_run,my_messgae):
                self.my_run = my_run
                self.my_messgae = my_messgae
                threading.Thread.__init__(self)
        def run(self):
            print('{0}..start.. {1}'.format(self.my_run,self.getName(),))
            self.my_run(self.my_messgae)
            print("%s...end.... %s"%(self.my_run,self.getName(),))