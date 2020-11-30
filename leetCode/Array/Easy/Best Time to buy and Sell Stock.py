
def maxProfit(prices):
    result = 0
    min_price = prices[0]

    for i in range(len(prices)):
        result = max(result, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return result


def maxProfit2(prices):
    max_profit = 0
    min_price_so_far = float('inf')
    i = 1
    for current_price in prices:
        min_price_so_far = min(min_price_so_far, current_price)
        print(f'day{i}')
        profit = current_price - min_price_so_far
        print(f'{current_price} {min_price_so_far}')
        print(profit)

        max_profit = max(max_profit, profit)
        i += 1
    return max_profit


# Dynamic programming:
def maxProfit3(prices):
    dp = [0] * len(prices)
    min_price = prices[0]

    for i in range(len(prices)):
        dp[i] = max(dp[i - 1], prices[i] - min_price)
        print(dp)
        min_price = min(min_price, prices[i])

    return dp[-1]


a = list(map(int, input().split()))
print(maxProfit3(a))






