from metod1 import *
from metod2 import *
import timeit

primes_to_test = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331,39916801, 479001599, 87178291199, 99194853094755497, 790738119649411319]

k = 5

def test_method1(primes_to_test):
    for prime in primes_to_test:
        is_prime(prime)

def test_method2(primes_to_test):
    for prime in primes_to_test:
        miller_rabin(prime, k)

print(timeit.timeit(lambda: test_method1(primes_to_test), number=1))
print(timeit.timeit(lambda: test_method2(primes_to_test), number=1))
print(f"Probability for error on method 2 is at most {2**(-k)}")