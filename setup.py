import os
import sys
import sysconfig
platform = sysconfig.get_platform()
from distutils.core import setup, Extension

# Adapted from http://stackoverflow.com/questions/11010151
class lazy_list(list):
    def __init__(self, callback):
        self._list = None
        self.callback = callback

    @property
    def list(self):
        if self._list is None:
            self._list = self.callback()
        return self._list

    def __iter__(self):
        for e in self.list:
            yield e

    def __getitem__(self, i):
        return self.list[i]

    def __len__(self):
        return len(self.list)

if sys.platform == 'darwin':
    from distutils import sysconfig as distsysconfig
    vars = distsysconfig.get_config_vars()
    vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-dynamiclib')

setup(
    name='pyadder',
    packages=[
        'pyadder',
    ],
    setup_requires=[
        'cython',
    ],
    ext_modules = lazy_list(ext_modules),
    include_dirs=['adder'],
)
