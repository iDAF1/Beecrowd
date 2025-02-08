#! /bin/python3.12
# -*- coding: utf-8 -*-
a        = float(input())
b        = float(input())
c        = float(input())
a_weight = 2
b_weight = 3
c_weight = 5
media    = (((a * a_weight) + (b * b_weight) + (c * c_weight))
         / (a_weight + b_weight + c_weight))
print(f'MEDIA = {media:.1f}')
