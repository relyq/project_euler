# things i learned 
# https://en.wikipedia.org/wiki/Prime_number
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://en.wikipedia.org/wiki/Primality_test
# https://en.wikipedia.org/wiki/Sieve_of_Atkin 

import argparse
import timeit

parser = argparse.ArgumentParser(description="finds highest prime factors")
parser.add_argument("integer", type=int, help="integer to find its factors")
parser.add_argument("-a", "--all", action="store_true", help="show all factors (could take a long time for large numbers)")
parser.add_argument("-p", "--primes", action="store_true", help="show all prime factors")

def find_primes(limit):
    list = []
    if limit <= 2:
        list.append(2)
        return list

    for i in range(2, limit):
        div_flag = False
        for j in range(2, i-1):
            if not i%j:
                div_flag = True
        if not div_flag:
            list.append(i)
    return list

def find_factors(x):
    list = []
    for i in range(2, x):
        if not x%i:
            list.append(i)
            x = x / i
            if i > x:
                break
    return list

def sieve(limit):
    list = []
    # 1
    list.append(2)
    for i in range(3, limit+1):
        if i%2:
            list.append(i)
    # 2
    x = list[0]
    # 3, 4
    while x**2 < limit:
        y = x**2
        try:
            list.remove(y)
        except ValueError:
            pass
        while y < limit:
            y += x
            try:
                list.remove(y)
            except ValueError:
                pass
        # no pointer arithmetic in python - lame
        x = list[list.index(x)+1]
    # 5
    return list

def find_next_prime(prime):
    next = prime
    i = 0
    while(next <= prime):
        next = sieve(next+i)[-1]
        i += 1
    return next

# this actually finds the smallest prime factor
def find_smallest_factor(x):
    factor = 2
    while x%factor:
        factor = find_next_prime(factor)    
    return factor 

# and this actually finds all prime factors
def find_prime_factors(x):
    factors = {}
    while(x!=1):
        print("find_prime_factors: x = {}".format(x))
        smallest = find_smallest_factor(x)
        if smallest in factors:
            factors[smallest] += 1
        else:
            factors[smallest] = 1

        x = x / smallest
    return factors

def is_prime(x):
    for i in range(2, x-1):
        if not x%i:
            return False
    return True

# kind of useless
def filter_primes(list):
    primes = []
    for i in list:
        if is_prime(i):
            primes.append(i)
    return primes

def performance_test():
    sieve_primes = sieve(args.integer)
    print("sieve primes below {}:".format(args.integer))
    print(sieve_primes, end="\n\n")

    print("sieve performance:")
    print(timeit.timeit("sieve(args.integer)", setup="from __main__ import sieve; from __main__ import args", number=100)/100, end="\n\n")

    brute_primes = find_primes(args.integer)
    print("brute forced primes below {}".format(args.integer))
    print(brute_primes, end="\n\n")

    print("brute force performance:")
    print(timeit.timeit("find_primes(args.integer)", setup="from __main__ import find_primes; from __main__ import args", number=100)/100, end="\n\n")

args = parser.parse_args()

#performance_test()

#primes = find_prime_factors(args.integer)

if args.all:
    factors = find_factors(args.integer)
    print("all factors of {}:".format(args.integer))
    print(factors, end="\n\n")
if args.primes:
    print("all prime factors of {}:".format(args.integer))
    #print(primes, end="\n\n")

#print("largest prime factor of {}:".format(args.integer))
#print(list(primes)[-1])

