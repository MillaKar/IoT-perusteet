import utime
import machine

external_led = machine.Pin(15, machine.Pin.OUT)

while True:
    external_led.toggle()
    utime.sleep(1)
