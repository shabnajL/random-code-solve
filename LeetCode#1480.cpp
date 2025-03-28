//1480. Running Sum of 1D Array
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result(nums.size());
        result[0] = nums[0];
        
        for(int i=1; i<nums.size(); i++){
            result[i] = nums[i] + result[i-1];
        }

        return result;

    }

/* 
//method-2:
      for(int i=1;i<nums.size(); i++){
            nums[i] += nums[i-1];
        }

        return nums;

*/
};
