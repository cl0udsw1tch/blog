class Solution {
public:
    int findMaxK(vector<int>& nums) {
        
        
        sort(nums.begin(), nums.end(), std::less<int>());
        int left = 0, right = nums.size() - 1;

        while (left < right)
        {
            if (nums[right] > -1 * nums[left]) right--;
            else if (nums[right] < -1 * nums[left]) left ++;
            else return nums[right];
        }

        return -1;
    }
};