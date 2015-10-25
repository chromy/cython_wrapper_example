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
