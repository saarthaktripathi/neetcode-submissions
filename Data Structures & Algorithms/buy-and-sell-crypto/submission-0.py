class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatest_profit= 0
        buy_price = prices[0]
        # [10, 1, 5, 6, 7, 1]
        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
                continue
                
            profit = prices[i] - buy_price
            greatest_profit = max(profit, greatest_profit)
        return greatest_profit