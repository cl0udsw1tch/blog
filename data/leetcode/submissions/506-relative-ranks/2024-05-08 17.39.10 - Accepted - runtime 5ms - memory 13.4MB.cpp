class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> scores(score.size());
        for (int i = 0; i < score.size(); i++)
        {
            pair<int, int> pr = {score[i], i};
            scores[i] = pr;
        }
        sort(scores.begin(), scores.end(), [](const pair<int, int>& first, const pair<int, int>& second) -> bool
        {
            return first.first > second.first;
        });
        vector<string> r(score.size());
        if (score.size() > 0)
        {
            r[scores[0].second] = "Gold Medal";

        }
        if (score.size() > 1)
        {
            r[scores[1].second] = "Silver Medal";

        }
        if (score.size() > 2)
        {
            
            r[scores[2].second] = "Bronze Medal";
        }
        for (int i = 3; i < score.size(); i++)
        {
            r[scores[i].second] = std::to_string(i+1);
        }
        return r;
    }
};