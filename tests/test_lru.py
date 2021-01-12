#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import lru_cache
@lru_cache(n)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(33)