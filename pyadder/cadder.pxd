# distutils: language = c++
# distutils: libraries = adder
# distutils: sources = ../adder/adder.cc
# distutils: extra_link_args= -L.

# from libcpp cimport bool

cdef extern from "adder.h":
    int add(int a, int b)
