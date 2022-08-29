#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = correct(tuple_a)
    t2 = correct(tuple_b)
    new = ((t1[0] + t2[0]), t1[1] + t2[1])
    return new
def correct(tup):
    if len(tup) == 0:
        return (0,0)
    elif len(tup) == 1:
        return (tup[0], 0)
    return (tup[0],tup[1])
