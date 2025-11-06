## 412. Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """ 
        answer = []
        i = 1
        while(i<=n):
            if i%3 == 0 and i%5 == 0:
                answer.append("FizzBuzz")
            elif i%3 == 0:
                answer.append("Fizz")
            elif i%5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
            i = i + 1
        """

        answer = []
        
        i = 1
        while(i<=n):
            checkAnswer = ""
            
            if i%3 == 0:
                checkAnswer += "Fizz"
            if i%5 == 0:
                checkAnswer += "Buzz"
            if not checkAnswer:
                checkAnswer += str(i) 
            
            answer.append(checkAnswer)
            i = i + 1
        
        return answer
            

        
            

        
