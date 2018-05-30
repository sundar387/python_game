from karel import *

start()

seq=[1,5,3,2,4,2]

for i in seq:
    move()
    for x in range(i):
        put_beeper()
move()
stop()
    
