import machine
import time
time.sleep(0.1) # Wait for USB to become ready

led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    ###
    #led_onboard.value(1)
    #time.sleep(1)
    #led_onboard.value(0)
    #time.sleep(1)
    ###
    led_onboard.toggle()
    time.sleep(1)


