import machine
import utime
import dht

sensor = dht.DHT22(machine.Pin(15))

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {:.1f}C".format(temperature))
        print("Humidity: {:.1f}%".format(humidity))
    except OSError as e:
        print("Sensor read error", e)

    utime.sleep(2)