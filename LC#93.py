# 93. Restore IP Addresses
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # checking for non-leading zero numbers
        def check(start: int, end: int) -> int:
            if (s[start] == "0" and start != end): 
                return False
            return 0<= int(s[start: end + 1]) <= 255

        def dfs(i: int):
            current_string_length = len(current_part)
            #print(current_string_length)
            
            if (i >= string_length and current_string_length==4):
                chunk_list.append(".".join(current_part))
                #print(chunk_list)
                return

            if (i >= string_length or current_string_length>=4):
                #print("executing if 2")
                return

            for j in range(i, min(i+3, string_length)):
                #print("executing for loop")
                if check(i, j):
                    #print(check(i, j))
                    current_part.append(s[i: j+ 1])
                    #print(current_part)
        
                    dfs(j + 1)

                    current_part.pop()

        string_length = len(s)
        # print(string_length)
        chunk_list = []
        current_part = []

        dfs(0)

        return chunk_list
