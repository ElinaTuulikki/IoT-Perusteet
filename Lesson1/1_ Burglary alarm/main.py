import machine
import utime

# PIR liikeanturi kytketty GP28
pir = machine.Pin(28, machine.Pin.IN)

while True:
    if pir.value() == 1:
        print("Movement detected!")
    else:
        print("No movement")

    utime.sleep(1)   # mittaa kerran sekunnissa
