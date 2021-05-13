# all prime number from 2 to n 

import math

def generate_primes(n):
    primes = [True]*(n+1)
    primes[0] = False 
    primes[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]==True:
            for j in range(i*i, n+1, i):
                primes[j] = False

    for i in range(0, len(primes)):
        if primes[i]==True:
            print(i, end = ' ')

    print("\n")

    # return primes

# print(generate_primes(50))

generate_primes(50)

