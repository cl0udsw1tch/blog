class Solution {
public:
    int findMaxLength(vector<int>& nums) {

        int sz = nums.size();
        if (sz < 2)
        {
            return 0;
        }
        if (sz == 2)
        {
            return nums[0] + nums[1] == 1 ? 2 : 0;
        }

        vector<int> Q(sz, 0);
        std::unordered_map<int, int> Q_inv;

        // state array, Q[i] is state after taking action A(q) : Q -> Q defined by
        // A(q) = q_{i - 1} + L(nums[i]) where L(i) : {0, 1} -> {-1, 1}
        Q[0] = nums[0] ?  1 : -1; 

        for (int i = 1; i < sz; i++)
        {
            Q[i] = Q[i - 1] + (nums[i] ? 1 : -1);
        }

        // Q^{-1} wont be well defined in the usual case where there is a contiguous
        // subarray, since Q(i_start) = Q(i_end) => Q is not injective, 
        // However, creating Q^{-1} by iterating backwards means the start index
        // overrides the end index, then we can iterate forward over the end indices.
        for (int i = sz - 1; i > -1; i--)
        {
            Q_inv[Q[i]] = i;
        }
        // State s_0 occurs before any action, thus the corresponding action idx is -1
        Q_inv[0] = -1; 

        int maxLen = 0;
        // iterating over the end indices
        for (int i = 0; i < sz; i++)
        {
            int currLen = i - Q_inv[Q[i]]; // i.e end index - start index
            if (currLen > maxLen)
            {
                maxLen = currLen;
            }
            
        }
        return maxLen;
    }
};