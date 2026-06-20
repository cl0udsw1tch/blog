class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int ptr1 = 0;
        int total = 0;
        while (ptr1 < nums.size())
        {
            int ptr2 = ptr1;
            int currSum = 1;
            while (ptr2 < nums.size())
            {
     
                currSum *= nums[ptr2];
                if (currSum < k)
                {
                    total++;
                }
                else
                {
                    break;
                }
                ptr2++;
            }
            ptr1++;
        }
        return total;
    }
};