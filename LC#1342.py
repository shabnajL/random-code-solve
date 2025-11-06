## 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        countSteps = 0
        while(num!=0):
            if(num%2 == 0): 
                num = num/2
            
            else:
                num = num - 1
            countSteps += 1

        return countSteps
