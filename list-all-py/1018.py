#! /bin/python3.12
# -*- coding: utf-8 -*-
banknotes = [100, 50, 20, 10, 5, 2, 1]
N         = int(input())
print(N)
for note in banknotes:
    count = N // note
    N = N % note 
    print(f"{count} nota(s) de R$ {note},00")
