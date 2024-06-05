### Leetcode#345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        #s = list(s.lower())
        s = list(s)
        #print(s)
        vowels = {'a', 'e', 'i', 'o','u','A','E','I','O','U'}
        start = 0
        end = len(s) - 1
        #print(start,end)
        while(start<end):
            if(s[start] in vowels and s[end]  in vowels):
                s[start], s[end] = s[end], s[start]
                start = start + 1
                end = end - 1
            elif(s[start] in vowels):
                end = end - 1
            else:
                start = start +1
        #print(s)
        #print("".join(s))
        return "".join(s)
        
