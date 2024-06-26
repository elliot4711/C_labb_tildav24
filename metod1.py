from math import isqrt
def is_prime(n: int) -> bool:
    """
    Code sourced from wikipedia: https://en.wikipedia.org/wiki/Primality_test#Miller%E2%80%93Rabin_and_Solovay%E2%80%93Strassen_primality_test
    """

    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(1000003))