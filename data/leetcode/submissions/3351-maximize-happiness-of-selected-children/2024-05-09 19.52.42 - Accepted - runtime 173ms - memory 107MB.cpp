class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), std::greater<int>());
        long long r = 0;
        for (int i = 0; i < k; i++)
        {
            r += max(0, happiness[i] - i);
        }
        return r;
    }
};