#! /bin/python3.12
# -*- coding: utf-8 -*-
x, y = map(float,  input().split())
table_items = {
    1.0: 4.00,
    2.0: 4.50,
    3.0: 5.00,
    4.0: 2.00,
    5.0: 1.50,
}
print(f'Total: R$ {y * table_items[x]:.2f}')
