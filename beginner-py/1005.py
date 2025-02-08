#! /bin/python3.12
# -*- coding: utf-8 -*-
a        = float(input())
b        = float(input())
a_weight = 3.5
b_weight = 7.5
media = (((a * a_weight) + (b * b_weight)) / (a_weight + b_weight))
print(f'MEDIA = {media:.5f}')
