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

# From: http://stackoverflow.com/questions/14320220
def distutils_dir_name(dname):
    """Returns the name of a distutils build directory"""
    f = "{dirname}.{platform}-{version[0]}.{version[1]}"
    return f.format(dirname=dname,
                    platform=platform,
                    version=sys.version_info)

def get_lib_folder():
    return os.path.abspath(os.path.join('build', distutils_dir_name('lib')))

# Build the shared library.
libadder = Extension('libadder',
    sources = [
        'adder/adder.cc',
    ],
    language = 'c++',
    # If you want assert to work.
    # undef_macros=['NDEBUG'],
)



def ext_modules():
    from Cython.Build import cythonize
    cython_modules = cythonize('pyadder/*.pyx')
    print cython_modules[0].sources
    return cython_modules

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
