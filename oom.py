#!/usr/bin/env python3


dic = {}

i = 1
while True:
    dic[i] = i + 1
    i += 1
    bag = set(str(int(i)))
    if bag == {'1', '0'}:
        print(i)
