## LC # 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        if(num == 0):
            return 0
        elif(num>=1 and num<=9):
            return num
        elif(num%9==0):
            return 9
        else:
            return (num%9)

"""
## TESTCASES
38
0
157
258
1098
1111
6799
9999
===================
"""
