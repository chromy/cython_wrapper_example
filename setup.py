import os
import sys
import sysconfig
platform = sysconfig.get_platform()

from setuptools import setup
from setuptools.extension import Extension

import pickle

USE_CYTHON = False
if '--use-cython' in sys.argv:
    USE_CYTHON = True
    sys.argv.remove('--use-cython')

def store(extensions):
    with open('extensions.pickle', 'w') as f:
        pickle.dump(extensions, f)

def load():
    with open('extensions.pickle') as f:
        return pickle.load(f)

def no_cythonize(extensions):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in ('.pyx', '.py'):
                if extension.language == 'c++':
                    ext = '.cpp'
                else:
                    ext = '.c'
                sfile = path + ext
            sources.append(sfile)
        extension.sources[:] = sources
    return extensions

def cythonize(*args, **kwargs):
    from Cython.Build import cythonize
    return cythonize(*args, **kwargs)

def ext_modules(*args, **kwargs):
    if USE_CYTHON:
        extensions = cythonize(*args, **kwargs)
        store(extensions)
        return extensions
    else:
        extensions = load()
        return no_cythonize(extensions)

setup(
    name='pyadder',
    packages=[
        'pyadder',
    ],
    setup_requires=[
        'cython',
    ],
    ext_modules = ext_modules([
        Extension('adder', sources=['pyadder/adder.pyx'], language='c++'),
    ]),
)

