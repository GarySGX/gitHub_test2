# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:09:27 2020

@author: GarySGX
"""

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

f = logged(f)
print("hello")
print(f.__name__)


print("docstring starts")
print(f.__doc__)
