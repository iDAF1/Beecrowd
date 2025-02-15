#! /bin/python3.12
# -*- coding: utf-8 -*-
name        = input()
salary      = float(input())
month_money = float(input())
total       = (salary + (month_money * (15/100)))
print(f'TOTAL = R$ {total:.2f}')
