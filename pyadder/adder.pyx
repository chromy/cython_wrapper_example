# distutils: language = c++
# distutils: sources = adder/adder.cc
cimport cadder

def add(a, b):
    return cadder.add(a, b)
