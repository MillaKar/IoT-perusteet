import utime
import machine

red = machine.Pin(15, machine.Pin.OUT)
yellow = machine.Pin(14, machine.Pin.OUT)
green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

def traffic_lights():
    while True:
        if button.value() == 1:
            red.value(1)
            yellow.value(0)
            green.value(0)
            buzzer.value(1)
            utime.sleep(3)
            buzzer.value(0)
        else:
            red.value(1)
            yellow.value(0)
            green.value(0)
            utime.sleep(2)
            
            red.value(0)
            yellow.value(1)
            green.value(0)
            utime.sleep(1)
            
            red.value(0)
            yellow.value(0)
            green.value(1)
            utime.sleep(2)

traffic_lights()