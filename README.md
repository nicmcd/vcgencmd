# vcgencmd - Native Python binding for vcgencmd tool

## Summary

'vcgencmd' is a command line tool designed by Broadcom used on the Raspberry Pi.
This Python package is a native binding to that tool. Currently only a portion
of the 'vcgencmd' command line tool is supported.

## Install

vcgencmd is compatible with both Python2.7+ and Python3.x. The raspberry pi I
have has python 3.2 installed. These instructions will be for that. You can
substitute the python and pip commands accordingly for other versions.
The installer requires the `setuptools` package.

### Requirements
Pip (Python 3 version):
```bash
sudo apt-get install python3-pip
```
Setuptools (Python 3 version):
```bash
sudo pip-3.2 install setuptools
```

### Python package manager (PIP)
Install globally:
```bash
sudo pip-3.2 install git+https://github.com/nicmcd/vcgencmd.git
```
Install locally:
```bash
pip-3.2 install --user git+https://github.com/nicmcd/vcgencmd.git
```

### Source installation
Install globally:
```bash
sudo python3 setup.py install
```
Install locally:
```bash
python3 setup.py install --user
```

## Uninstall
```bash
sudo pip-3.2 uninstall vcgencmd
```

## Usage
TODO(nicmcd)
