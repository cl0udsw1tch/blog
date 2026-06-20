
class Solution {

public:

    int dfs(vector<vector<int>>& grid, int i, int j, map<pair<int, int>, int>& ee)
    {
        if (!grid[i][j] || ee[{i, j}]) return 0;

        int total = grid[i][j];
        ee[{i, j}] = 1;
        int a = 0;
        

        if (i - 1 > -1 && grid[i - 1][j])
        {
            a = max(a, dfs(grid, i - 1, j, ee));
        }
        if (i + 1 < grid.size() && grid[i + 1][j])
        {
            a = max(a, dfs(grid, i + 1, j, ee));
        }
        if (j - 1 > -1 && grid[i][j - 1])
        {
            a = max(a, dfs(grid, i, j - 1, ee));
        }
        if (j + 1 < grid[0].size() && grid[i][j + 1])
        {
            a = max(a, dfs(grid, i, j + 1, ee));
        }

        ee[{i, j}] = 0;

        return total + a;
    }
    int getMaximumGold(vector<vector<int>>& grid) {
        std::map<std::pair<int, int>, int> visited;
        int total = 0;
        int rows = grid.size();
        int cols = grid[0].size();

        map<pair<int, int>, int> ee;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                total = max(total, dfs(grid, i, j, ee)); 
            }
        }
        return total;
    }
};