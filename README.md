# PyProxy - Very Simple TCP/UDP Proxy

## About
PyProxy is a very simple TCP/UDP pure Python proxy.
It can be easily extended for custom data handling logic.

## Usage
```cmd
>pyproxy.py -h
usage: pyproxy.py [-h] (--tcp | --udp) -s SRC -d DST [-q | -v]

TCP/UPD proxy.

optional arguments:
  -h, --help         show this help message and exit
  --tcp              TCP proxy
  --udp              UDP proxy
  -s SRC, --src SRC  Source IP and port, i.e.: 127.0.0.1:8000
  -d DST, --dst DST  Destination IP and port, i.e.: 127.0.0.1:8888
  -q, --quiet        Be quiet
  -v, --verbose      Be loud
```

### Custom data handlers
Proxy uses two data handlers for incoming and outgoing data.
By default both are set to identity function. 
```python
LOCAL_DATA_HANDLER = lambda x:x
REMOTE_DATA_HANDLER = lambda x:x
```

One can easily implement own rules. It might be very useful while testing network applications.
```python
def custom_data_handler(data):
    # code goes here
    pass
    
LOCAL_DATA_HANDLER = custom_data_handler
REMOTE_DATA_HANDLER = lambda x:'constant_value'
```

## License
Code is released under [MIT license](https://github.com/rsc-dev/pyproxy/blob/master/LICENSE) © [Radoslaw '[rsc]' Matusiak](https://rm2084.blogspot.com/).