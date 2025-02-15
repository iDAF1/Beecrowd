# !/usr/bin/python3.12
# -*- coding: utf-8 -*-
A, B, C = map(float, input().split())
sides   = sorted([A, B, C], reverse=True)
A, B, C = sides[0], sides[1], sides[2]
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
