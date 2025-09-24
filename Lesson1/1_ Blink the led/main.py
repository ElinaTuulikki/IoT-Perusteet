import machine
import time
time.sleep(0.1) # Wait for USB to become ready

led_onboard = machine.Pin(15, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    time.sleep(1)
