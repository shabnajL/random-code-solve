## 29. Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 1:
            return dividend
        if dividend == -2147483648 and divisor ==-1:
            return 2147483647
        og_dvd, og_dvs = dividend, divisor
        dvd = -dividend if dividend>0 else dividend
        dvs = -divisor if divisor>0 else divisor
        # print("(dvd, dvs) = ", dvd,"\t", dvs)
        result = 0
        while(dvd <= dvs):
            tempdvs = dvs
            count = 1

            while(dvd <= tempdvs+tempdvs):
                tempdvs += tempdvs
                count += count
                # print("(tempdvs, count) = ", tempdvs,"\t", count)
            
            dvd -= tempdvs
            result += count
            # print("(dvd, result) = ", dvd,"\t", result)
        
        if (og_dvs>0 and og_dvd<0) or (og_dvs<0 and og_dvd>0):
            result = -result
        return result
