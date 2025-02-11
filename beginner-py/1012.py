#! /bin/python3.12
# -*- coding: utf-8 -*-
a, b, c = map(float,input().split())
output  = [
    f'TRIANGULO: {((a * c) / 2):.3f}',
    f'CIRCULO: {(c**2 * 3.14159):.3f}',
    f'TRAPEZIO: { (((a + b) * c)/ 2):.3f}',
    f'QUADRADO: {(b**2):.3f}',
    f'RETANGULO: {(a * b):.3f}',
] 
for i in output: print(i)
