import machine
import utime
import urandom

from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from machine import I2C, Pin

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

time_start = 0

def button_handler(pin):
    button.irq(handler=None)
    reaction_time = utime.ticks_diff(utime.ticks_ms(), time_start)

    print("Your reaction time was " + str(reaction_time) + " milliseconds")
    print("Program complete.")

    lcd.clear()
    lcd.putstr("Reaction Time:\n")
    lcd.putstr(str(reaction_time) + " ms")

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
time_start = utime.ticks_ms()

button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
