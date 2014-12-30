# issue 121

class Solution:

    # @param prices, a list of integer

    # @return an integer

    def maxProfit(self, prices):

        if len(prices) < 2:

            return 0

        min_v=prices[0]

        max_profit=0

        for i in prices:

            min_v=min(min_v,i)

            max_profit=max(max_profit,i-min_v)

        return max_profit
