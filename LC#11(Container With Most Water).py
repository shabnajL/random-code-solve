class Solution:
    def maxArea(self, height: List[int]) -> int:
        #print(height)
        startPoint = 0
        endPoint = len(height) - 1
        
        area = 0
        newArea = 0
        while(startPoint < endPoint):
            width = endPoint - startPoint
            newArea = min(height[startPoint], height[endPoint]) * width

            area = max(newArea, area)

            if(height[endPoint]<= height[startPoint]):
                endPoint = endPoint - 1
            else:
                startPoint = startPoint + 1 

        return area
