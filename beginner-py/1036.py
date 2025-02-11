#!/bin/python3.12
# -*- coding: utf-8 -*-
a, b, c = map(float,input().split())
delta   = (b**2) - 4 * a * c
if a != 0 and delta >= 0:
    bhaskara_R1 = (-b + (delta ** 0.5)) / (2 * a)
    bhaskara_R2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f'R1 = {bhaskara_R1:.5f}')
    print(f'R2 = {bhaskara_R2:.5f}')
else:
    print('Impossivel calcular')

