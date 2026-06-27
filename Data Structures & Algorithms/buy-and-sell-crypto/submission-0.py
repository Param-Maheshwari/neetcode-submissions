class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer approach
        l, r = 0,1  # l = buy, r = sell
        maxP = 0

        while r < len(prices): # r will go thru whole array
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r # So that we can buy at lowest rate
            r += 1
        return maxP
