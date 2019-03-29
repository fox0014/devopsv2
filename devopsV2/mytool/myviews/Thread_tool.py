import threading
import time

class MyThread(threading.Thread):
        def __init__(self,my_run,*args,**kwargs):
                self.my_run = my_run
                self.my_option = args
                self.my_option2 = kwargs
                threading.Thread.__init__(self)
        def run(self):
#            print('{0}..start.. {1}'.format(self.my_run,self.getName(),))
            self.my_run(self.my_option,self.my_option2)
 #           print("%s...end.... %s"%(self.my_run,self.getName(),))