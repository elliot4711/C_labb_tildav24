import random

def miller_rabin(n, k=5):
    # Code generated using chatGPT, prompt
    # can you help me make a probabilistic test using python to decide if a number is prime. The probability of error should be able to be reduced by repeating the test with several independently 
    # chosen values of a; for two commonly used tests, for any composite n at least half the a's detect n's compositeness, so k repetitions reduce the error probability 
    # to at most 4^-k, which can be made arbitrarily small by increasing k.
    """
    Miller-Rabin primality test
    Args:
        n (int): Number to test for primality
        k (int): Number of iterations for the test
    Returns:
        bool: True if n is likely to be prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform the test k times
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Example usage

if __name__ == "__main__":
    number_to_test = 9  # Change this to the number you want to test
    iterations = 1  # Number of iterations for the test
    is_prime = miller_rabin(number_to_test, iterations)
    if is_prime:
        print(f"{number_to_test} is likely to be prime.")
    else:
        print(f"{number_to_test} is composite.")


