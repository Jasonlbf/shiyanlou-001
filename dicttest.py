#!/usr/bin/env python3

import sys

arg = sys.argv[1:]
dic = {}

for a in arg:
    lis = a.split(':')
    dic[lis[0]] = lis[1]

for key,value in dic.items():
    print('ID:{} Name:{}'.format(key,value))
