#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1 # decrementing n in each iteration
    return result
if len(sys.argv) < 2: # this handles the case when no command-line argument is provided
    sys.exit(1)
f = factorial(int(sys.argv[1]))
print(f)
