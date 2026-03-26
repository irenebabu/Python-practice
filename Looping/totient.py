"""
Find totient
Euler's totient counts the positive integers up to a given integer 
that are relatively prime (i.e., share no common factors other than 1)
 eg : 10 ---> 1,3,7,9 are co-prime numbers of 10 (totient = 4)
 the GCD of 10 and 3 is 1 ,10 & 7 gcd is 1 
"""
  
def gcd(a, b):   #or from math import gcd ,use gcd () directly
    gcd = 0
    smallest = min(a, b)
    for i in range(1, smallest + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def eulers_totient(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

print(eulers_totient(10))
print(eulers_totient(9))