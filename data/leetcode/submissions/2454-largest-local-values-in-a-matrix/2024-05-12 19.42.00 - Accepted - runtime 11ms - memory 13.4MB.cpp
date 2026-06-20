class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int sz = grid.size();
        vector<vector<int>> r(sz - 2, vector<int>{});
        for (auto& elem : r)
        {
            elem.reserve(sz - 2);
        }
        for (int i = 0; i < sz - 2; i++)
        {
            for (int j = 0; j < sz - 2; j++)
            {
                int currMax = 0;
                for (int k = 0; k < 3; k++)
                {
                    for (int l = 0; l < 3; l++)
                    {
                        currMax = max(currMax, grid[i + k][j + l]);
                    }
                }
                r[i].push_back(currMax);
            }
        }
        return r;
    }
};