class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        profitdict = {}
        profitdict[prices[0]] = 0
        for i in range(1, len(prices), 1):
            higher = False
            new_price = prices[i]
            # establish min of 0 for specified price if it didn't have one
            if(new_price not in profitdict):
                profitdict[new_price] = 0
            for price in sorted(profitdict):
                if(not higher):
                    #check if higher, and run logic if it is
                    if(price > new_price):
                        higher = True
                        # run higher logic
                        if(profitdict[price] > profitdict[new_price]):
                            profitdict[new_price] = profitdict[price]
                    else: #run lower logic
                        new_profit = profitdict[price] + (new_price - price)
                        if(new_profit > profitdict[new_price]):
                            profitdict[new_price] = new_profit
                else: # run higher logic
                    if(profitdict[price] > profitdict[new_price]):
                            profitdict[new_price] = profitdict[price]
        #check max profit for each price min to find max profit possible overall
        for price in profitdict:
            if(profitdict[price] > maxprofit):
                maxprofit = profitdict[price]
        return maxprofit