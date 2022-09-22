def maxProfit(prices):
    
    profit = 0
    low = prices[0]
    high = prices[0]

    
    
    for i in range(len(prices)):
        
        if  prices[i] > high:
            high = prices[i]
        else:
            profit += high - low
            low = prices[i]
    return profit

prices = [7,6,4,3,2,1]


print(maxProfit(prices))