# 2. Modify the LED-Button program so the LED blinks twice when the button is pressed.

from machine import Pin
import time

button_pin = Pin(14, Pin.IN, Pin.PULL_UP)
led_pin = Pin(15, Pin.OUT)



def blink_twice():
    led_pin.value(1)
    time.sleep(.3)
    led_pin.value(0)
    time.sleep(.3)
    
    led_pin.value(1)
    time.sleep(.3)
    led_pin.value(0)
    time.sleep(.3)

while True:
    if button_pin.value() == 0:
        blink_twice()
    else:
        led_pin.value(0)
    time.sleep(.1)
