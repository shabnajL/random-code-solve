## 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        # if(len(magazine) < len(ransomNote)):
        #    result = False
        if Counter(magazine) >= Counter(ransomNote):
            result = True
        return result
