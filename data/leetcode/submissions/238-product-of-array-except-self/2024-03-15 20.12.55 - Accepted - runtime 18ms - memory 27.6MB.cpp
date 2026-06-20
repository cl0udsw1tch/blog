class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int sz = nums.size();
        if (sz == 2)
        {
            return {nums[1], nums[0]};
        }

        vector<int> prefix(sz, 1), suffix(sz, 1);
        for (int i = 1; i < sz; i++)
        {
            prefix[i] = prefix[i - 1] * nums[i - 1];
            suffix[sz - i - 1] = suffix[sz - i] * nums[sz - i];
        }
        for (int i = 0; i < sz; i++)
        {
            nums[i] = prefix[i] * suffix[i];
        }
        return nums;


    }
};