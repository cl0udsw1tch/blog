class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int size = nums.size();
        int maxLen = 0;
        int i = 0;
        int j = 0;
        std::map<int, int> freqs;
        std::map<int, std::queue<int>> firstIdx;
        int len = 0;
        while (i < size && j < size)
        {
            while (j < size && freqs[nums[j]] + 1<=k)
            {
     
                firstIdx[nums[j]].push(j);
                freqs[nums[j]]++;
                j++;
                len++;
            }
            maxLen = len > maxLen ? len : maxLen;
            if (j >= size)
            {
                return maxLen;
            }
            int newStart = firstIdx[nums[j]].front() + 1; 

            if ((newStart + maxLen) >= size) // maxLen + 1 subarray starting at i + j cannot be created 
            {
                return maxLen;
            }
            for (int l = i; l < newStart; l++)
            {
                freqs[nums[l]]--;
                firstIdx[nums[l]].pop();
            }
            len-=newStart-i;
            i = newStart;
        }
        return maxLen;
    }
};