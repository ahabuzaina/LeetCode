class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = 0
        res = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[least]:
                least = i
            res = max(res, prices[i]-prices[least])
        return res
            
        
        