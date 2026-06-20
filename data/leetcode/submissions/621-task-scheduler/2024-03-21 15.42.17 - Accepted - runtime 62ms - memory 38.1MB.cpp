bool sorter(const pair<char, int>& first, const pair<char, int>& second)
{
    return first.second > second.second;
}
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        if (n == 0)
        {
            return tasks.size();
        }
        int numIntervals = 0;
        vector<pair<char, int>> remaining;
        std::map<char, int> idxs;
        for (char c : tasks)
        {
            if (idxs.find(c) == idxs.end())
            {
                idxs[c] = remaining.size();
                remaining.push_back({c, 1});
            }
            else
            {
                remaining[idxs[c]].second++;
            }
        }
        int taskCount = remaining.size();
        if (taskCount == 1)
        {
            return tasks.size() * (n + 1) - n;
        }
        std::sort(remaining.begin(), remaining.end(), sorter);
        int i=0;
        int lenLast = 0;
        while (i < remaining.size() && remaining[i].second == remaining[0].second)
        {
            i++;
        }
        lenLast = i;
    
        return std::max((int)tasks.size(), (remaining[0].second - 1) * (n + 1) + lenLast);
    }
};
