"""W1-4 Translate C++ to Python.

Assigned variant for Ha Xuan Tinh: Sieve of Eratosthenes.

The Sieve of Eratosthenes finds all prime numbers up to a given limit n.
"""


def primes_up_to(n: int) -> list[int]:
    """Return all prime numbers up to n using the Sieve of Eratosthenes.

    Differences from a C++ implementation:
    - Python uses a plain list of booleans instead of std::vector<bool>.
    - List comprehension replaces a C++ for-loop that builds the output vector.
    - No manual memory management or size declarations are needed.
    - int(n ** 0.5) replaces std::sqrt() with an explicit cast to int.

    Args:
        n: Upper bound (inclusive) to search for primes.

    Returns:
        A sorted list of all prime numbers in the range [2, n].
        Returns an empty list when n < 2.
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
