"""
    buy-sell stock

            [7, 1, 5, 3, 6, 4] ==> 5
            [9, 7, 6, 4, 3, 1] ==> 0
"""


def max_profit(prices):
    cur_max, max_so_far = 0, 0
    loop_count = 0
    for loop_count, index in enumerate(range(1, len(prices))):
        cur_max = max(0, cur_max + prices[index] - prices[index - 1])
        max_so_far = max(max_so_far, cur_max)

    return f"{max_so_far} => {loop_count}"


print(max_profit([7, 1, 5, 3, 6, 4]))
