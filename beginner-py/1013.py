#! /bin/pydoc3.12
# -*- coding: utf-8 -*-
a, b, c  = map(int,input().split())
maiorA_B = ( a + b + abs(a-b)) / 2
maiorALL = int(((maiorA_B + c + abs(maiorA_B - c)) / 2))
print(f'{maiorALL} eh o maior')

 
