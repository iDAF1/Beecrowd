#!/bin/python3.12
# -*- coding: utf-8 -*-
A, B, C = map(float, input().split())
if A + B > C and A + C > B and B + C > A:
    perimeter = A + B + C
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = (A + B) * C / 2
    print(f"Area = {area:.1f}")
