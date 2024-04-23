from metod1 import *
from metod2 import *
import timeit

numbers_to_test = [2, 3, 6, 12, 17, 18, 22, 38, 331999, 331222, 332222, 333333, 393919, 919393, 914000, 39916801, 30000000, 87178291199, 87178291190, 87178291200, 
                    99194853094755498, 99194453094755496, 99194853014755497]

k = 20 #260 för typ jämnt

def test_method1(primes_to_test):
    for prime in primes_to_test:
        is_prime(prime)

def test_method2(primes_to_test):
    for prime in primes_to_test:
        miller_rabin(prime, k)

timea = (timeit.timeit(lambda: test_method1(numbers_to_test), number=1000) / 1000)
timeb = (timeit.timeit(lambda: test_method2(numbers_to_test), number=1000) / 1000)

print(timea)
print(timeb)
print(f"Time difference for a list containing normal numbers and primes, method 1 is {timea/timeb}x slower")


time1 = (timeit.timeit(lambda: is_prime(1000000000193), number=1000) / 1000)
time2 = (timeit.timeit(lambda: is_prime(100000000003), number=1000) / 1000)
time3 = (timeit.timeit(lambda: is_prime(10000000019), number=1000) / 1000)

time4 = (timeit.timeit(lambda: miller_rabin(1000000000193, k), number=1000) / 1000)
time5 = (timeit.timeit(lambda: miller_rabin(100000000003, k), number=1000) / 1000)
time6 = (timeit.timeit(lambda: miller_rabin(10000000019, k), number=1000) / 1000)

print(time1)
print(time2)
print(time3)
print(time4)
print(time5)
print(time6)

print(f"Probability for error on method 2 is at most {(4**(-k)) * 100}%")

print(f"Time coefficient for 10x higher prime with method 1 is {time1/time2}")
print(f"Time coefficient for 100x higher prime with method 1 is {time1/time3}")

print(f"Time coefficient for 10x higher prime with method 2 is {time4/time5}")
print(f"Time coefficient for 100x higher prime with method 2 is {time4/time6}")
