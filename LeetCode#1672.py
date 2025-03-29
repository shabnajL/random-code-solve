//1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for customer in accounts:
            currentcustomer_wealth = 0

            for wealth in customer:
                currentcustomer_wealth = currentcustomer_wealth + wealth

            maxWealth = max(maxWealth, currentcustomer_wealth)
        

        return maxWealth
        
        
