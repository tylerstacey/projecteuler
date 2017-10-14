"""
PROJECT EULER - PROBLEM 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys

def main():
    print 'Problem 1 - Project Euler'
    integers = 0
    integersSum = 0
    while integers < 1000:
        if integers % 3 == 0:
            print 'The multiple of 3 is ' + str(integers)
            integersSum += integers
        elif integers % 5 == 0:
            print 'The multiple of 5 is ' + str(integers)
            integersSum += integers
        print 'The running sum is ' + str(integersSum)
        integers += 1
if __name__ == '__main__':
    main()
