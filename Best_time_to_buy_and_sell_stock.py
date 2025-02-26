def maxProfit(prices):
        profit=0
        max_profit=0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                if prices[i]<prices[j]:
                    profit=prices[j]-prices[i]
                if profit>max_profit:
                    max_profit=profit
        return max_profit
if __name__=="__main__":
     prices=[7,1,5,3,6,4]
     print(maxProfit(prices))
