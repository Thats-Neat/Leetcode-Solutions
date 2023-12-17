#
# [121] Best Time to Buy and Sell Stock
#

class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        profit = 0

        for price in prices[1:]:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)

        return profit
