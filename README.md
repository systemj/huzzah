
# Adafruit Feather HUZZAH Stuff

## Reference:
https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266
http://micropython.org/download/#esp8266

### BEST:
*https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html*


### install esptool
```
sudo pacman -S esptool
```

### flash firmware:
Erase flash just in case (help resolve problems)
```
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool --port /dev/ttyUSB1 --baud 460800 write_flash --flash_size=detect 0 esp8266-20180511-v1.9.4.bin
```

### Interactive access:

Micropython interpreter
Paste mode (disable auto-indent) = Ctrl-E, then Ctrl-D to end

```
sudo screen /dev/ttyUSB0 115200
```

## Quick Load Code:

Create main.py on your machine, then serve it locally:
```
python -m http.server
```

```
# connect to wifi
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('ssid', 'pass')

# fetch source file
import urequests as requests
r = requests.get("http://your_ip:8000/main.py")

# save file locally
f = open('main.py', 'w')
f.write(r.text)
f.close()

```

## notes


### Pin/LED access:
(ok if on/off backwards)
```
>>> import machine
>>> pin = machine.Pin(2, machine.Pin.OUT)
>>> pin.on()
>>> pin.off()
>>> def toggle(p):
...     p.value(not p.value())

```

#### Feather LEDs:

```
blue = machine.Pin(2, machine.Pin.OUT)
red  = machine.Pin(0, machine.Pin.OUT)
```

### Network
Reference: https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html

```
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('ssid', 'pass')

sta_if.isconnected()
sta_if.ifconfig()
('192.168.0.101', '255.255.255.0', '192.168.0.1', '192.168.0.1')
>>> 
```


```
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
```


### https:
https://github.com/micropython/micropython/blob/master/examples/network/http_client_ssl.py

```
try:
    import usocket as _socket
except:
    import _socket
try:
    import ussl as ssl
except:
    import ssl


def main(use_stream=True):
    s = _socket.socket()

    ai = _socket.getaddrinfo("google.com", 443)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        s.write(b"GET / HTTP/1.0\r\n\r\n")
        print(s.read(4096))
    else:
        # MicroPython SSLSocket objects implement only stream interface, not
        # socket interface
        s.send(b"GET / HTTP/1.0\r\n\r\n")
        print(s.recv(4096))

    s.close()
    machine.deepsleep()


main()
```


