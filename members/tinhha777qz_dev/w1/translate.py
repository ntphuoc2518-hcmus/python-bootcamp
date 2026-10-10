"""W1-4 Translate C++ to Python.

Assigned personal variant for Ha Xuan Tinh: Linear search.
"""


def linear_search(a: list[int], key: int) -> int:
    """Return index of key in list a, or -1 if absent.

    Difference from C++:
    Unlike C++ where std::vector<int> requires indexing with bounds check,
    Python provides idiomatic iteration using enumerate() and handles
    lists dynamically without needing const references like const std::vector<int>&.
    """
    for index, val in enumerate(a):
        if val == key:
            return index
    return -1


def primes_up_to(n: int) -> list[int]:
    """Return all prime numbers up to n using the Sieve of Eratosthenes.

    Provided for compatibility with the initial test suite.
    """
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]
