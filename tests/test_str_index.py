#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

a = re.finditer('aa', 'aaa')
for i in a:
    print(i.span()[0])
