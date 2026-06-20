class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        int size = nums.size();
        int first = nums[0];
        map<int, int> freqs;
        vector<int> atMostK;
        vector<int> atMostKMinus1;
        int start = 0;
        int currNumUnique = 0;

        // FOR ATMOSTK
        for (int end = 0; end < size; end++)
        {
            if (!freqs[nums[end]])
            {
                currNumUnique++;
            }
            freqs[nums[end]]++;
            if (currNumUnique <= k)
            {
                atMostK.push_back(start);
            }
            else
            {
                
                while (currNumUnique > k)
                {
                    freqs[nums[start]]--;
                    if (!freqs[nums[start]])
                    {
                        currNumUnique--;
                    }
                    start++;
                }
                atMostK.push_back(start);
            }

        }

        // FOR ATMOSTKMINUS1
        currNumUnique = 0;
        freqs = {};
        start=0;
        for (int end = 0; end < size; end++)
        {
            if (!freqs[nums[end]])
            {
                currNumUnique++;
            }
            freqs[nums[end]]++;
            if (currNumUnique <= k - 1)
            {
                atMostKMinus1.push_back(start);
            }
            else
            {
                while (currNumUnique > k - 1)
                {
                    freqs[nums[start]]--;
                    if (!freqs[nums[start]])
                    {
                        currNumUnique--;
                    }
                    start++;
                }

                atMostKMinus1.push_back(start);
            }

        }

        int numGood = 0;
        for (int i= 0; i < nums.size(); i++)
        {
            numGood += atMostKMinus1[i] - atMostK[i];
        }

        return numGood;
    }
};