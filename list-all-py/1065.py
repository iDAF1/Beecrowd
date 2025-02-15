#! /usr/bin/python3.12
# -*- coding: utf-8 -*-
input_list = [abs(int(input())) for i in range(5)]
count      = 0
for i in input_list:
    if i%2==0:
        count += 1
print(f'{count} valores pares')
