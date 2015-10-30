Cython: An Example
==================

[![Build Status](https://travis-ci.org/chromy/cython_wrapper_example.svg?branch=master)](https://travis-ci.org/chromy/cython_wrapper_example)


Wrapping a C++ library using Cython in a way that it can be installed and used
transparently by an average Python user in an unnecessarily novel experience.
This example points out (and helps you avoid) some of the more interesting pitfalls.

In particular this project shows how to wrap C++/C code that is present in your
source repository, maybe because you are writing it just for this project or maybe
because it is an existing library that you plan to copy into your project or
include as a git submodule. It doesn't show how to wrap a library that a user
will or has installed separately (say via brew or apt-get) although some parts
may still be applicable.

Walkthrough
-----------

As an example we'll write a Python wrapper for the following piece of C++:

```cpp
int add(int a, int b) {
    return a + b;
}
```

Normally we'll be wrapping a much larger amount of code so to keep our project
organised we'll keep all the C++/C code in a sub-directory. In this case we're
pretending to wrap a C++ library named `adder` so all the code will go under a
directory named [adder](adder). This directory will contain implementation
files (in this case only [adder.cpp](adder/adder.cpp)) and header files (in this case
only [adder.h](adder/adder.h)).

We've seen [adder.cpp](adder/adder.cpp) above and the contents of
[adder.h](adder/adder.h) is quite predictable:

```cpp
int add(int a, int b);
```

Since our library is so simple writing the Cython wrapper is relatively
straight forward. Again to keep things organised we'll put everything into
a sub-directory: [pyadder](pyadder) this will be our module (in Python users
will write `import pyadder` to access our wrapped module).


Distributing your Wrapper
-------------------------

Since Cython code must be compiled to C (which in turn must be compiled
to produce a binary) distributing a package that uses Cython is much more
complicated than distributing a pure-Python package and slightly more
complicated than distributing a Python package with a C extension.
There are two common strategies for distributing your wrapper, the first
approach is perform the Cython-to-C conversion 'user-side'; when users install
your package (e.g. by running `pip install pyadder`) `setup.py` will use Cython
to convert the Cython code to C alternatively we 

Directory layout
---------------
```
cython_wrapper_example
│── setup.py
└── adder
    ├───subfolder1
    └───folder2
```

Common problems
---------------

### Error: missing cimport in module 'mypxdfile': mydirectory/mypyxfile.pyx ###

This is a slightly confusing error message is probably due to a
missing `__init__.py` file under `mydirectory`.
