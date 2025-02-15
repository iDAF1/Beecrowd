#! /bin/python3.12
# -*- coding: utf-8 -*-
N       = int(input())
hours   = (N // 3600)
minutes = ((N % 3600) // 60)
seconds = (N % 60)
print(f"{hours}:{minutes}:{seconds}")

