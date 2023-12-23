class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        diff = 0
        for i in range(1, len(prices), 1):
            if(diff < (prices[i] - lowest)):
                diff = prices[i] - lowest
            if(lowest > prices[i]):
                lowest = prices[i]
        return diff