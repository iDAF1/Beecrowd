#! /bin/python3.12
# -*- coding: utf-8 -*-
x = float(input())
if not (x < 0 or x > 100):
    if x <= 25.0:
        print('Intervalo [0,25]')
    elif 25.0 < x <= 50.0:
        print('Intervalo (25,50]')
    elif 50.0 < x <= 75.0:
        print('Intervalo (50,75]')
    elif 75.0 < x <= 100.0:
        print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
