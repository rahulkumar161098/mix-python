# ************* Garbage collection ****************
#  Garbage collection is to release memory when the object is no longer in used. This system destroys to unused object and reuse its memory slots for new object.

import time
import gc

print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())



# eng
class Outer:
    def __init__(self):
        print('outer class initializing')
    def __del__(self):
        print('distroy call')

t1=Outer()
# t1=None
time.sleep(5)
print('process end')