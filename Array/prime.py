# 204. Count Primes
# Medium
# Topics
# Companies
# Hint
# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
n = 10

# import numpy as np
import sympy as si
# print(si.isprime(n))
nl=0
for i in range(0,n):
    if si.isprime(i):
        nl=nl+1
print(nl)

def countPrimes(n):
        
        c = 0
        for num in range(2, n):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                c += 1
        return c
  


# def prime_no(n):
