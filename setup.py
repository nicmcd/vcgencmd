import codecs
import re
import os
import sys

try:
  from setuptools import setup
except:
  print('please install setuptools using pip:')
  print('  <pip> install setuptools')
  sys.exit(-1)

def find_version(*file_paths):
    version_file = codecs.open(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), *file_paths), 'r').read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


setup(
    name='vcgencmd',
    version=find_version('vcgencmd', '__init__.py'),
    description='Native binding for vcgencmd',
    author='Nic McDonald',
    author_email='nicci02@hotmail.com',
    license='Apache License Version 2.0',
    url='http://github.com/nicmcd/vcgencmd',
    packages=['vcgencmd'],
    scripts=[],
    install_requires=[],
    )
