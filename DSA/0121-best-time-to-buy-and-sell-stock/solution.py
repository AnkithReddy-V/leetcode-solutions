class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float('inf')
        profit = 0
        for i in range(0, len(prices)):
            if(bp > prices[i]):
                bp = prices[i]
            elif(prices[i] - bp > profit):
                profit = prices[i] - bp
        return profit

        
