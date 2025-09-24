import machine
import time
import dht
import network
import urequests

# ThingSpeak API key ja URL
THINGSPEAK_API_KEY = "OMA_API_KEY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# WiFi-tiedot
WIFI_SSID = "OMA_WIFI"
WIFI_PASS = "OMA_SALASANA"

# Yhdistä WiFiin
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print("Connecting to WiFi...")
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        time.sleep(1)
print("WiFi connected:", wlan.ifconfig())

# Initialize DHT22 sensor on GP15
sensor = dht.DHT22(machine.Pin(15))

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature: {:.1f}°C".format(temperature))
        print("Humidity: {:.1f}%".format(humidity))

        # Lähetä data ThingSpeakille
        params = "api_key={}&field1={}&field2={}".format(
            THINGSPEAK_API_KEY, temperature, humidity
        )
        response = urequests.post(THINGSPEAK_URL, data=params)
        print("ThingSpeak response:", response.text)
        response.close()

    except OSError as e:
        print("Sensor read error:", e)

    time.sleep(20)  # ThingSpeak sallii max 1 päivityksen / 15 sek
