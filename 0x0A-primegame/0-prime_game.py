#!/usr/bin/python3
"""Prime Game"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [0] * (n + 1)
    for i in range(1, n + 1):
        primes[i] = primes[i - 1]
        if is_prime(i):
            primes[i] += 1
    winner = 0
    for n in nums:
        winner ^= (primes[n] % 2 == 0)
    return "Ben" if winner else "Maria"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
