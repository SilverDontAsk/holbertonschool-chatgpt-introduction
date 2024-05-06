#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number.

    Parameters:
    - n: an integer for which factorial is to be calculated

    Returns:
    - The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# this will check if argument count is correct
if len(sys.argv) != 2:
    sys.exit(1) # exit with a non-zero status to indicate an error
# this will convert the argument to integer and handle any value error
try:
    num = int(sys.argv[1])
except ValueError:
    sys.exit(1)
# check if the argument is a non-negative integer
if num < 0:
    sys.exit(1)
f = factorial(num)
print(f)
