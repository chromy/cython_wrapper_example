# distutils: language = c++
# distutils: include_dirs = adder

cdef extern from "adder.h":
    int add(int a, int b)
