# https://en.wikipedia.org/wiki/Prime_number
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://en.wikipedia.org/wiki/Primality_test
# https://en.wikipedia.org/wiki/Sieve_of_Atkin 

import argparse

parser = argparse.ArgumentParser(description="finds highest prime factors")
parser.add_argument("integer", type=int, help="integer to find its factors")
parser.add_argument("-a", "--all", action="store_true", help="show all factors")

def find_factors(x):
    list = []
    i = 2
    while i <= x:
        if not x%i:
            list.append(i)
            x = x / i
        i += 1
    return list

args = parser.parse_args()

factors = find_factors(args.integer)

if args.all:
    factors = find_factors(args.integer)
    print("all factors of {}:".format(args.integer))
    print(factors, end="\n\n")

print("largest prime factor of {}:".format(args.integer))
print(list(factors)[-1])
