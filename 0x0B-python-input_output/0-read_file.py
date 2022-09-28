#!/usr/bin/python3
""" reades a file"""

def read_file(filename=""):
    """args"""
    
    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
