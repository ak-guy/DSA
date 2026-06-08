'''
121. Best Time to Buy and Sell Stock

Intuition: The intuition behind this solution relies on a greedy historical low strategy, 
where you treat the stock market timeline as a one-way journey to find the single biggest 
price jump. Instead of checking every possible combination of buying and selling days, you 
move forward through time step-by-step while maintaining two pieces of information: the 
absolute cheapest price you have seen so far (min_buy) and the highest profit recorded yet 
(profit). On any given day, you ask a simple question: "If I were forced to sell my stock 
right now, how much money would I make assuming I bought it on the best possible day in the 
past?" You calculate this potential payout (prices[i] - min_buy), update your global record 
if it beats your previous best, and then immediately update your historical floor 
(min_buy = min(min_buy, prices[i])) so that you are fully prepared to capitalize on even 
larger price spikes further down the line.
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        min_buy = prices[0]
        profit = 0

        for i in range(1,n):
            profit = max(profit, prices[i]-min_buy)
            min_buy = min(min_buy, prices[i])
        
        return profit
