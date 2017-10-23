'''You will be given a list of stock prices for a given day and your goal is to return the maximum profit 
that could have been made by buying a stock at the given price and then selling the stock later on. 
For example if the input is: [45, 24, 35, 31, 40, 38, 11] then your program should return 16 because if you bought the stock at $24 and sold it at $40, 
a profit of $16 was made and this is the largest profit that could be made. If no profit could have been made, return -1.'''

def StockPicker(arr):
    buy_price=0
    sell_price=0
    max_profit=-1
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
           buy_price=arr[i]
           sell_price=arr[j]
           if sell_price>buy_price:
               profit=sell_price-buy_price
               if profit>max_profit:
                  max_profit=profit
           else: 
               j+=1
    i+=1
    return max_profit


print StockPicker([44, 30, 24, 32, 35, 30, 40, 38, 15])