# Copyright 2014 Nic McDonald. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''vcgencmd: native binding for vcgencmd (Raspberry Pi).'''

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import subprocess
import sys


def __do_command(command):
  return subprocess.check_output(command).decode('utf-8')

def __lookup(command, src_list, src):
  src = src.lower()

  if src not in src_list:
    raise InvalidArgumentError('{0} must be one of {1}'.format(
        src, src_list))

  return __do_command(['vcgencmd', command, src])


__kFreqSrcs = ['arm', 'core', 'h264', 'isp', 'v3d', 'uart', 'pwm', 'emmc',
               'pixel', 'vec', 'hdmi', 'dpi']

def frequency_sources():
  return __kFreqSrcs

def measure_clock(src):
  output = __lookup('measure_clock', __kFreqSrcs, src)
  return int(output[output.find('=') + 1:].strip())


__kVoltSrcs = ['core', 'sdram_c', 'sdram_i', 'sdram_p']

def voltage_sources():
  return __kVoltSrcs

def measure_volts(src):
  output = __lookup('measure_volts', __kVoltSrcs, src)
  return float(output[output.find('=') + 1:].strip().rstrip('V'))


def measure_temp():
  output = __lookup('measure_temp', [''], '')
  return float(output[output.find('=') + 1:].strip().rstrip('\'C'))


__kCodecSrcs = ['h264', 'mpg2', 'wvc1', 'mpg4', 'mjpg', 'wmv9']

def codec_sources():
  return __kCodecSrcs

def codec_enabled(src):
  output = __lookup('codec_enabled', __kCodecSrcs, src)
  status = output[output.find('=') + 1:].strip()
  if status == 'disabled':
    return False
  if status == 'enabled':
    return True
  raise Exception('unknown output \'{0}\''.format(status))


__kMemSrcs = ['arm', 'gpu']

def memory_sources():
  return __kMemSrcs

def get_mem(src):
  output = __lookup('get_mem', __kMemSrcs, src)
  mem = output[output.find('=') + 1:].strip()
  num = int(mem[:-1])
  if mem[-1] == 'M':
    return num * 1024 * 1024
  if mem[-1] == 'G':
    return num * 1024 * 1024 * 1024
  raise Exception('unknown unit \'{0}\''.format(mem[-1]))
