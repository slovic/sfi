#-*- coding: utf-8 -*-

import sys

def fizzbazz(number) :
    if float(number) % 3 == 0: print number, "fizz"
    elif float(number) % 5 == 0: print number,  "buzz"
    elif float(number) % 15 == 0: print number,  "fizzbuzz"
    else: print number
for arg in sys.argv:
    if arg != "fizzbuz.py": 
        fizzbazz(arg)    
