import RPi.GPIO as gp
import time

def listen():
    print("Listening for RF signals:")
    recieve()
    return True

def recieve():
    gp.setmode(gp.BCM)
    gp.setup(16, gp.IN)
    gp.setup([20,21], gp.OUT, initial=gp.HIGH)
    
    count = 0

    while count != 400000000:
        rcv = gp.input(16)
        if rcv == 1:
            count += 1
            print(count)

    gp.cleanup()
