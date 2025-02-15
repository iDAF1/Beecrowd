#! /usr/bin/python3.12
# -*- coding: utf-8 -*-
n =  int(input())
if 5 < n < 2000:
    for i in range(2,n + 1,2):
        print(f'{i}^2 = {i**2}')
