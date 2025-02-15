#!/bin/python3.12
# -*- coding: utf-8 -*-
days      = int(input())
years     = (days // 365)
months    = (days % 365) // 30
days_left = (days % 365) % 30
output    = [
    f"{years} ano(s)",
    f"{months} mes(es)",
    f"{days_left} dia(s)",
]
for i in output:
    print(i)

