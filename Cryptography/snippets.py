from math import isqrt
from random import randint


def gcd(a: int, b: int) -> int:
    """Calculates the least common divisor using the Euclidean algorithm

    Complexities:
        Time  - O(log(min(a,b))
        Space - O(1)
    """
    while b:
        a, b = b, a % b
    return a


def bin_pow(x: int, n: int, mod: int) -> int:
    """Binary exponentiation modulo

    Algorithm:
        To naively raise a to a power of n, it suffices to perform n multiplications:
            a^n = a*a*a..*a
        In this case, we need O(n) operations, but if you look closely, you can see that we are
        calculating the same values repeatedly, for example:
            2^8 = 2*2*2*2*2*2*2*2.
        That is, the expression 2*2*2*2 is counted twice, instead you can rewrite the expression as:
            2^8 = 2*2*2*2*2*2*2*2 = (2*2*2*2)^2 = ((2*2)^2)^2 = ((2^2)^2)^2
        If the power to which you want to raise is odd, you can turn the following trick:
            a^n = a*a^(n-1)
        In total, we have the following relation:
            a^n = a*a^(n-1) if n is odd
            a^n = (a^(n/2))^2 otherwise

    Complexities:
        Time  - O(log(n))
        Space - O(1)
    """
    power = 1
    x = x % mod

    while n > 0:
        if n % 2:
            power = (power * x) % mod
            n -= 1
        else:
            x = (x ** 2) % mod
            n //= 2

    return power % mod


def totient(n: int) -> int:
    """Calculates Euler's totient function

    Euler's function φ(n) is equal to the number of numbers less than n
    that are coprime (greatest common divisor is 1) with n.

    Euler function properties:
        φ(p^n) = p^n - p^(n-1)
        φ(n)   = n-1           if n is a prime number
        φ(n*m) = φ(n)*φ(m)     if m and n are mutually prime

    Complexities:
        Time  - O(n*log(n))
        Space - O(1)
    """
    return sum(gcd(i, n) == 1 for i in range(1, n))


def is_prime(num: int) -> bool:
    """Checks if a number is prime by enumeration of divisors

    Complexities:
        Time  - O(√n)
        Space - O(1)

    Args:
        num (int): number to check for primality

    Returns:
        bool: True if the number is prime, false otherwise.
    """
    if num <= 1:  # Negative numbers and the numbers 0 and 1 are not prime
        return False

    for divisor in range(2, isqrt(num) + 1):
        if not num % divisor:
            return False

    return True


def is_prime_optimized(num: int) -> bool:
    """Checks if a number is prime using 6k±1 divisor optimization

    Algorithm:
        If the number is not divisible by either 2 or 3 (basic prime numbers), then it makes no sense
        to check every second and every third divisor, instead of the divisors for the number 751:
            2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
        It is enough to check the divisibility by 2 and 3 and cross out the corresponding divisors:
            _ _ _ 5 _ 7 _ _ _ 11 _ 13 _ _ _ 17 _ 19 _ _ _ 23 _ 25 _ _
        This shows that it is enough to check the divisibility for every 6k±1 divisor

    Complexities:
        Time  - O(√n)
        Space - O(1)
    """
    if num <= 1:  # Negative numbers and the numbers 0 and 1 are not prime
        return False
    if num <= 3:  # Numbers 2 and 3 are basic primes
        return True
    if not num % 2 or not num % 3:
        return False

    divisor = 6
    while divisor * divisor <= num:
        if not num % (divisor - 1) or not num % (divisor + 1):
            return False
        divisor = divisor + 6

    return isqrt(num) ** 2 != num


def fermat_test(n: int, n_repeats: int = 100) -> bool:
    """Tests whether a number is prime using the Fermat primality test

    Euler's theorem:
        a^φ(m) ≡ 1 mod m, if a and m are mutually prime, where φ - Euler's totient function

    Algorithm:
        If the number n is prime, then any number in the range [2, n-2] must satisfy Euler's theorem,
        that is, tests with random numbers give a sufficiently high probability that the number n is prime.

    Complexities:
        Time  - O(k*log(n))
        Space - O(1)
    """
    if n == 1 or not n & 1:  # One and even numbers are not prime
        return False

    if n == 2 or n == 3:  # Base cases
        return True

    for _ in range(n_repeats):
        if bin_pow(randint(2, n - 2), n - 1, n) != 1:
            return False

    return True
