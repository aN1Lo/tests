import os
import time

# os.system('C:\\Progra~1\\Genymobile\\Genymotion\\player.exe --vm-name \"test\"')
f = open('tests.log', 'w')
# os.open('/dev/null', os.O_RDWR)
f.write('Executing all tests.\n')
f.flush()
f.close()


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("\x1b[33m\nElapsed time: {:.3f} min.\x1b[0m".format((time.time() - self._startTime)/60))
        f1 = open('C:\\Users\\Adm\\Downloads\\tests\\tests.log', 'a')
        f1.write("\nElapsed time: {:.3f} min.\n".format((time.time() - self._startTime)/60))
        f1.flush()
        f1.close()

with Profiler() as p:
    if __name__ == "__main__":
        from autotests import *

# lock.release()
