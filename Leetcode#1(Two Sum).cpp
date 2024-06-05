// Leetcode 1. two sum
class Solution {
public:
    vector<int> twoSum(vector<int> nums, int target) {
        int sum = 0;
        for(int i=0;i<(nums.size()-1);i++){
            for(int j=1+i; j<nums.size();j++){
                sum = nums[i] + nums[j];
                //cout<<sum;
                if(sum == target){
                    return {i,j};
                }
            }
        }
        return {};
    }
};
