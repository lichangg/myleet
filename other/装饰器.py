#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools


def deco(fun):
    def wrap(*args, **kwargs):
        print('前')
        a = fun(*args, **kwargs)
        print('后')
        return a
    return wrap

@deco
def f(name):
    return name
c=f('lic')
print(c)

def counter(cls):
    obj_list = []
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        print(1)
    return wrapper
