#!/usr/bin/python3
"""
Determines fewest coins needed to meet a given amount
"""


def makeChange(coins, total):
    """
    Calculate minimum coins needed to make total
    Args:
        coins: list of coin values
        total: target amount
    Returns:
        Minimum coins needed or -1 if impossible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Initialize dp array with total + 1 (impossible value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build solution for each amount from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
