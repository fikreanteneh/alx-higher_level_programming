#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = set(my_list)
    sum = 0
    for i in newList:
        sum += i
    return sum
