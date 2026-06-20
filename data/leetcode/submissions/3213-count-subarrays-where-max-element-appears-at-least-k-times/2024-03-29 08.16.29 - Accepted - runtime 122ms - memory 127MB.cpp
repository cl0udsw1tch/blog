class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long count = 0;
        long long size = nums.size();
        if (size == 1 && k <= 1)
        {
            return 1;
        }
        long long start = 0, end = 0, first = 0;
        int max = *std::max_element(nums.begin(), nums.end());
        vector<long long> valid_idxs;
        for (long long i = 0; i < size; i++)
        {
            if (nums[i] == max)
            {
                valid_idxs.push_back(i);
            }
        }
        while ((start < size) && (first + k - 1 < valid_idxs.size()))
        {
            end = valid_idxs[first + k - 1];
            count += size - end;
            if (start == valid_idxs[first])
            {
                first++;
            }
            start++;
        }
        
        return count;
    }
};