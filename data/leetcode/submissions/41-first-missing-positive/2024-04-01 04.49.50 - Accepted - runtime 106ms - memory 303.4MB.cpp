class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
        long long max_e = *max_element(nums.begin(), nums.end());
        if (max_e < 1)
        {
            return 1;
        }
        vector<bool> hasElementAtIdx(max_e + 1, false);
        hasElementAtIdx[0] = true;
        int size = nums.size();
        for (int i = 0; i < size; i++)
        {
            if (nums[i] > 0)
            {
                hasElementAtIdx[nums[i]] = true;
            }
        }

        return find(hasElementAtIdx.begin(), hasElementAtIdx.end(), false) - hasElementAtIdx.begin();
        

    }
};