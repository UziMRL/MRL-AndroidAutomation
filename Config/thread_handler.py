
import threading
import subprocess

class thread_handler(threading.Thread):




    def __init__(self,str_,show_shell):
        self.show_shell = show_shell
        self.to_run = str_
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)
        self.lock = threading.Lock()


    def run(self):
        p = subprocess.Popen(self.to_run.split(),
                                 shell=self.show_shell,
                                 # stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        p.communicate()

        self.stdout, self.stderr = p.communicate()

# myclass = MyClass()
# myclass.start()
# myclass.join()
# print myclass.stdout



