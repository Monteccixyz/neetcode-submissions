class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0

        for i in range(len(prices)-1):
            for num in prices[i+1:]:
                best = max(best,num-prices[i])

        return best