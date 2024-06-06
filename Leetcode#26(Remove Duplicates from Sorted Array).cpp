// Leetcode#26. Remove Duplicates from Sorted Array
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //vector<int>& count;
        //sort(nums.begin(),nums.end());
        int j = 1;
        //count[0] = nums[0];
        for(int i = 1; i<nums.size();i++){
            if(nums[i] != nums[i-1])
            {
                //count.push_back(nums[i]);
                nums[j] = nums[i];
                j++;
            }  
        }
        return j;
    }
};
