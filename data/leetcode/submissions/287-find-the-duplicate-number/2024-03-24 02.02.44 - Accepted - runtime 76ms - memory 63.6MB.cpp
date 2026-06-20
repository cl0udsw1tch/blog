class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        bool buffer[100001];
        std::memset(buffer, false, sizeof(buffer) * sizeof(bool));
        for (int& num: nums)
        {
            if (buffer[num])
            {
                return num;
            }
            buffer[num]=true;
        }
       return nums[0];
    }
};