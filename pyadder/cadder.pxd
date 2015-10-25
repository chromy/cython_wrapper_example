# distutils: language = c++

# from libcpp cimport bool

cdef extern from "adder.h":
    int add(int a, int b)
