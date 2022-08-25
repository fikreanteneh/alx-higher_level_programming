#!/usr/bin/python3
for i in range(122, 96, -1):
    flag = False
    if i % 2 != 0:
        flag = True
    if flag:
        i = i - 32
    print("{}".format(chr(i)), end="")
