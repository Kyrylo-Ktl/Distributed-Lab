from snippets import bin_pow, is_prime, is_prime_optimized, fermat_test, totient

MOD = 10 ** 9 + 7


def task2(a: int) -> int:
    """Solves an equation of the form: a mod m = x, for x"""
    return a % MOD


def task3(a: int, b: int) -> int:
    """Solves an equation of the form: a^b mod m = x, for x"""
    return bin_pow(a, b, MOD)


def task4(a: int, b: int) -> int:
    """Solves an equation of the form: a*x ≡ b mod m, for x
    using Euler's theorem (for case when GCD(a, m) == 1):

    x ≡ (b * a^φ(n)-1) mod n
    """
    return (b * bin_pow(a, totient(MOD) - 1, MOD)) % MOD


def task5(a: int, b: int, check_is_prime=is_prime_optimized) -> int:
    """Returns the smallest prime number from an interval [a, b]

    Args:
        a (int): Range start, inclusive
        b (int): Range end, inclusive
        check_is_prime (Callable): primality test function

    Returns:
        (int): The smallest prime number in the interval, or -1 if the interval contains no primes

    """
    return next((num for num in range(a, b + 1) if check_is_prime(num)), -1)
