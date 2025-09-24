import utime
import machine

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)