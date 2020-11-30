# straight forward algorithm with O(n) time and O(1) space:
"""
For each day, there are 3 possible actions: buy, sell, nothing.
The action nothing can be interpreted at "sell then immediately buy.
So positive changes of prices are profitable
"""


def maxProfit(prices):

    max_profit = 0
    for i in range(len(prices) - 1):
        max_profit += max(prices[i + 1] - prices[i], 0)

    return max_profit


# another straight forward approach:
def maxProfit2(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


a = list(map(int, input().split()))
print(maxProfit2(a))
