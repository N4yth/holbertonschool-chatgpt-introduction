#!/usr/bin/python3
import sys

def factorial(n):
    """
    factorial - function that do the factorial of a number in recursive

    @n: the number to calcule

    Return: the number multiplie the return of the recursive
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)