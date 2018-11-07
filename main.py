# MicroPython!
import machine
import network
import time
try:
    import urequests as requests
except ImportError:
    import requests

ESSID = "essid"
PASSWORD = "pass"
URL = "http://192.168.0.100:3000/hooks/pPcAvXhmBa6f6vrin/cukx6ryaBE6wGz7WJPHiyjFJxKpjW3StDbcj5CXgcHrxZLPk"
JSON = {
  "username": "ESP8266",
  "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Micropython-logo.svg/2000px-Micropython-logo.svg.png",
  "text": "Test message"
}

def do_connect():
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(ESSID, PASSWORD)
    while not sta_if.isconnected():
      time.sleep_ms(100)
  print('network config:', sta_if.ifconfig())


def main(use_stream=True):
  do_connect()
  print('fetching URL...' + URL)
  r = requests.post(URL, json=JSON)
  print('going to sleep...')
  machine.deepsleep()


main()

