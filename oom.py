#!/usr/bin/env python3
from time import sleep


def oom():
    dic = {}

    i = 1
    while True:
        dic[i] = i + 1
        i += 1
        bag = set(str(int(i)))
        if bag == {'1', '0'}:
            print(i)
            sleep(0.5)


if __name__ == "__main__":
    oom()
