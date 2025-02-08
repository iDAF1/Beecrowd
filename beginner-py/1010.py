#! /bin/python3.12
# -*- coding: utf-8 -*-
x_code, x_unit, x_price = map(float, list(input().split()))
y_code, y_unit, y_price = map(float, list(input().split()))
value = (x_unit * x_price) + (y_unit * y_price)
print(f'VALOR A PAGAR: R$ {value:.2f}')
