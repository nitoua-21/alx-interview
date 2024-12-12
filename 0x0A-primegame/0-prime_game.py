#!/usr/bin/python3
"""
Module implementing the Prime Game challenge
"""


def isPrime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the Prime Game.

    Args:
        x (int): Number of rounds
        nums (list): List of n values for each round

    Returns:
        str: Name of the player with most wins, or None if no clear winner
    """
    # Validate input
    if x <= 0 or not nums:
        return None

    # Count Maria and Ben's wins
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        # No primes to pick
        if n < 2:
            ben_wins += 1
            continue

        # Create a set of remaining numbers
        numbers = set(range(1, n + 1))
        current_player = "Maria"

        # Continue until no primes remain
        while True:
            # Find available primes
            primes = [num for num in numbers if isPrime(num)]

            # No primes available
            if not primes:
                # If current player can't move, other player wins
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Pick smallest prime and remove it and its multiples
            prime = min(primes)
            numbers = {num for num in numbers if num % prime != 0}

            # Switch players
            current_player = "Ben" if current_player == "Maria" else "Maria"

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
