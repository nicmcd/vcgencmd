# vcgencmd - Native Python binding for RaspberryPi vcgencmd command-line tool

## Summary

'vcgencmd' is a command line tool designed by Broadcom used on the Raspberry Pi.
This Python package is a native binding to that tool. Currently only a portion
of the 'vcgencmd' command line tool is supported.

## Install

vcgencmd is compatible with both Python2.7+ and Python3.x. These instructions will be for Python 3.x. You can
substitute the python and pip commands accordingly for other versions.
The installer requires the `setuptools` package.

### Requirements
Pip (Python 3 version):
```bash
sudo apt-get install python3-pip
```
Setuptools (Python 3 version):
```bash
sudo pip3 install setuptools
```

### Python package manager (PIP)
Install globally:
```bash
sudo pip3 install git+https://github.com/nicmcd/vcgencmd.git
```
Install locally:
```bash
pip3 install --user git+https://github.com/nicmcd/vcgencmd.git
```

### Source installation
Install globally:
```bash
sudo pip3 install -e .
```
Install locally:
```bash
pip3 install -e . --user
```

## Uninstall
```bash
sudo pip3 uninstall vcgencmd
```

## Test/Command-Line
```bash
nic@raspberrypi:/tmp$ python3 -m vcgencmd
Clock Frequencies (Hz):
  arm       : 700000000
  core      : 250000000
  h264      : 250000000
  isp       : 250000000
  v3d       : 250000000
  uart      : 3000000
  pwm       : 0
  emmc      : 250000000
  pixel     : 25200000
  vec       : 0
  hdmi      : 163683000
  dpi       : 0
Voltages (V):
  core      : 1.2
  sdram_c   : 1.2
  sdram_i   : 1.2
  sdram_p   : 1.225
Temperatures (C):
            : 37.9
Codecs Enabled:
  h264      : False
  mpg2      : False
  wvc1      : False
  mpg4      : False
  mjpg      : False
  wmv9      : False
Memory Allocation (bytes):
  arm       : 469762048
  gpu       : 67108864
```

## Usage
```bash
nic@raspberrypi:/tmp$ python3
Python 3.2.3 (default, Mar  1 2013, 11:53:50)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import vcgencmd
>>> vcgencmd.frequency_sources()
['arm', 'core', 'h264', 'isp', 'v3d', 'uart', 'pwm', 'emmc', 'pixel', 'vec', 'hdmi', 'dpi']
>>> vcgencmd.measure_clock('arm')
700000000
>>> vcgencmd.measure_clock('hdmi')
163682000
>>> vcgencmd.voltage_sources()
['core', 'sdram_c', 'sdram_i', 'sdram_p']
>>> vcgencmd.measure_volts('core')
1.2
>>> vcgencmd.measure_volts('sdram_p')
1.225
>>> vcgencmd.measure_temp()
38.5
>>> vcgencmd.codec_sources()
['h264', 'mpg2', 'wvc1', 'mpg4', 'mjpg', 'wmv9']
>>> vcgencmd.codec_enabled('mpg4')
False
>>> vcgencmd.memory_sources()
['arm', 'gpu']
>>> vcgencmd.get_mem('arm')
469762048
>>>
``` 
