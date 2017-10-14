#coding=utf-8
"""
PROJECT EULER - PROBLEM 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.Find the largest palindrome
made from the product of two 3-digit numbers.
"""
import sys
def main():
    print 'Problem 4 - Project Euler'
    maxpal = 0
    for a in range(999, 99, -1):
        for b in range(a, 99, -1):
            prod = a * b
            if is_pal(prod) and prod > maxpal:
                maxpal = prod
    print maxpal
def is_pal(c):
    return int(str(c)[::-1]) == c
if __name__ == '__main__':
    main()
