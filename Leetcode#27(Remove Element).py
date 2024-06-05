### Leetcode 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #nums1 = [value for value in nums if value != val]
        length = len(nums)
        j = 0
        #new_nums = []
        for i in range(length):
            #print(i, nums[i], val)
            if nums[i] != val:
                #new_nums.append(nums[i])
                nums[j] = nums[i]
                j = j + 1
                #print(i, new_nums, val)
        #print(new_nums)
        #length = len(new_nums)
        return j
