
# Adafruit Feather HUZZAH Stuff
https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/overview

## Getting Started:
https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html

### Firmware Download:
http://micropython.org/download/#esp8266


## Quick Start (Linux)

### Download and flash the Micropython firmware.

#### install esptool
```
sudo pip install esptool adafruit-ampy
```

#### flash firmware:
Erase flash just in case (help resolve problems)
```
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20180511-v1.9.4.bin
```

### Interactive access:
Micropython interpreter
Paste mode (disable auto-indent) = Ctrl-E, then Ctrl-D to end
Ctrl-A k to exit screen (kill connecton)
```
sudo screen /dev/ttyUSB0 115200
```

## Load Code Over WiFi (only small files):
Create main.py on your machine, then serve it locally:
```
python -m http.server
```

### Download/Save 
(Via interactive interpreter)
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

## Load Code via ampy:
Reset Huzzah and Ctrl-C from serial connection if necessary to get to REPL prompt.
```
sudo ampy --port /dev/ttyUSB0 put main.py
```

### Other ampy functions:

#### List files:
```
sudo ampy --port /dev/ttyUSB0 ls
```

#### Get file (to stdout):
```
sudo ampy --port /dev/ttyUSB0 get main.py
```

#### Delete file:
```
sudo ampy --port /dev/ttyUSB0 rm main.py
```

## Random Notes

### Pin/LED access:
(ok if on/off backwards)
```
import machine
pin = machine.Pin(2, machine.Pin.OUT)
pin.on()
pin.off()
def toggle(p):
  p.value(not p.value())
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
True
sta_if.ifconfig()
('192.168.0.101', '255.255.255.0', '192.168.0.1', '192.168.0.1')
```

### Handy Connection Function
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


### http/https:
(via https://github.com/micropython/micropython-lib/blob/master/urequests/example_xively.py)
#### GET
```
import urequests as requests
r = requests.get("https://systemj.net/ascii.txt")
print(r.text)
r.close()
```

#### POST JSON
```
import urequests as requests
data = {"thing": "value"}
r = requests.post('https://api.example.com', json=data)
```

