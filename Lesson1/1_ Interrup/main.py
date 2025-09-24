import machine
import utime
import urandom

#Set up LED and button
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

#Global variables
time_start = 0

#Interrupt handler
def button_handler(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), time_start)
    print("Your reaction time was " + str(reaction_time) + " milliseconds")
    print("Program complete.")

#Signal user to get ready
led.value(1)
utime.sleep(urandom.uniform(5, 10))

#Turn off LED - signal to press the button
led.value(0)
time_start = utime.ticks_ms()

#Enable interrupt
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)