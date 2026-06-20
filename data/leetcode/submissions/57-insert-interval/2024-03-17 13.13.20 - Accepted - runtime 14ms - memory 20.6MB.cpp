class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {

        if (intervals.empty())
        {
            return {newInterval};
        }
        int startCoverIdx;
        int endCoverIdx;
        if (intervals.size() == 1)
        {
            startCoverIdx = endCoverIdx = 0;
        }
        else
        {
            int i = 0;
            while (newInterval[0] > intervals[i][1] && i < intervals.size()-1)
            {
                i++;
            }
            startCoverIdx = i;
            int j = intervals.size() - 1;
            while (newInterval[1] < intervals[j][0] && j > 0)
            {
                j--;
            }
            endCoverIdx = j;
        }

        vector<vector<int>> res;
        for (int j = 0; j < startCoverIdx; j++)
        {
            res.push_back(intervals[j]);
        }

        if (startCoverIdx < endCoverIdx) // distinct covers => both intersect 
        // argument by counterpositive:
        // (using the natural ordering of the covers)
        // suppose at least one non intersecting cover C_s (WLOG)
        // => C_s[0] > newInterval[1] OR C_s[1] < newInterval[0]
        // => C_s >= C_e (contractiction) OR C_s doesn't satisfy the condition for a startCover (a contradiction). 
        {
            int newStart = min(intervals[startCoverIdx][0], newInterval[0]);
            int newEnd = max(intervals[endCoverIdx][1], newInterval[1]);

            res.push_back({newStart, newEnd});

        }
        else if (startCoverIdx == endCoverIdx) // one cover 
        {
            if (newInterval[0] <= intervals[startCoverIdx][1] 
                && newInterval[1] >= intervals[startCoverIdx][0]) // intersection
            {
                int newStart = min(intervals[startCoverIdx][0], newInterval[0]);
                int newEnd = max(intervals[endCoverIdx][1], newInterval[1]);

                res.push_back({newStart, newEnd});
            }
            else // no intersction
            {
                if (intervals[startCoverIdx][1] < newInterval[0])
                {
                    res.push_back(intervals[startCoverIdx]);
                    res.push_back(newInterval);
                }
                else
                {
                    res.push_back(newInterval);
                    res.push_back(intervals[startCoverIdx]);
                }
            }
        }
        else // no cover
        {
            res.push_back(newInterval);
        }

        for (int j = endCoverIdx + 1; j < intervals.size(); j++)
        {
            res.push_back(intervals[j]);
        }

        return res;


    }
};