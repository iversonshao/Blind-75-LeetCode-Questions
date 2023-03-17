# Input一個array，裡面放股價
# output賺最大價差


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            # checking for lower buy value
            # way1
            # if (buy > prices[i]):
            #     buy = prices[i]

            # checking for higher profit
            # elif (prices[i] - buy > max_profit):
            #     max_profit = prices[i] - buy
            # way2
            buy = min(buy, prices[i])
            max_profit = max(max_profit, prices[i] - buy)
        return max_profit


# case1
# sol = Solution()
# res = sol.maxProfit([7, 1, 5, 3, 6, 4])
# print(res)

# case2
sol = Solution()
res = sol.maxProfit([7, 6, 4, 3, 1])
print(res)
