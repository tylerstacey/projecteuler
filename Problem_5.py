#coding=utf-8
"""
PROJECT EULER - PROBLEM 5
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""
import sys
def main():
    print 'Problem 5 - Project Euler'
    print lcmm(*range(1,20))
def gcd(a, b):
    #Return greatest common divisor using Euclid's Algorithm.
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    #Return lowest common multiple.
    return a * b // gcd(a, b)

def lcmm(*args):
    #Return lcm of args.
    return reduce(lcm, args)
if __name__ == '__main__':
    main()
