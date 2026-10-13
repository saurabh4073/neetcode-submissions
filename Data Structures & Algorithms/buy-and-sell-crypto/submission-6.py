class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        profit = 0
        l,r = 0,0
        while r<len(prices):
            if prices[r]>prices[l]:
                res = prices[r] - prices[l]
                profit = max(profit, res)
            else:
                l=r
            r+=1
        return profit