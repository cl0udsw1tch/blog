class Compared
{
public:
    bool operator() (const pair<int, int>& first, const pair<int, int>& second)
    {
        return (float)(first.first / first.second) > float(second.first / second.second);
    }
};

class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        vector<int> r;
        vector<pair<int, int>> h;
        for (int i = 0; i < arr.size() - 1; i++)
        {
            for (int j = i + 1; j < arr.size(); j++)
            {
                pair<int, int> p = {arr[i], arr[j]};
                h.push_back(p);
            }
        }

        sort(h.begin(), h.end(), [](const pair<int, int>& first, const pair<int, int>& second) -> bool
    {
        return ((float)first.first / (float)first.second) < ((float)second.first / (float)second.second);
    });

        r.push_back(h[k-1].first);
        r.push_back(h[k-1].second);

        return r;

    }
};