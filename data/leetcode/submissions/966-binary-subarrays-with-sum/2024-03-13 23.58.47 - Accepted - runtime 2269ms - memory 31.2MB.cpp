class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        
        int total = 0;
        int size = nums.size();

        for (int start = 0; start < size; start++)
        {
            int curr_sum = 0;
            if (nums[start] && size - start < goal - 1)
            {
                return total;
            }
            if (!nums[start] && size - start < goal)
            {
                return total;
            }
            for (int len = 0; len < size - start; len++)
            {   
                curr_sum += nums[start + len];

                if (curr_sum == goal)
                {
                    total++;
                }
                if (curr_sum > goal)
                {
                    break;
                }
            }
        }
        return total;
    }
};