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

from . import vcgencmd

import argparse
import sys


def __do(label, sources, function):
  print('{0}:'.format(label))
  for src in sources:
    if src == '':
      val = function()
    else:
      val = function(src)
    print('  {0}{1}: {2}'.format(
        src, ' ' * (10 - len(src)), str(val)))


def main(args):
  kTxtLen = 10

  __do('Clock Frequencies (Hz)',
       vcgencmd.frequency_sources(),
       vcgencmd.measure_clock)
  __do('Voltages (V)',
       vcgencmd.voltage_sources(),
       vcgencmd.measure_volts)
  __do('Temperatures (C)',
       [''],
       vcgencmd.measure_temp)
  __do('Codecs Enabled',
       vcgencmd.codec_sources(),
       vcgencmd.codec_enabled)
  __do('Memory Allocation (bytes)',
       vcgencmd.memory_sources(),
       vcgencmd.get_mem)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  args = parser.parse_args()
  sys.exit(main(args))
