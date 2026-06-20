class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int nrows = grid.size();
        int ncols = grid[0].size();
        for (int row = 0; row < nrows; row++)
        {
            if (!grid[row][0])
            {
                for (int col = 0; col < ncols; col++)
                {
                    grid[row][col] = !grid[row][col];
                }
            }
        }
        for (int col = 0; col < ncols; col++)
        {
            int sum = 0;
            for (int row = 0; row < nrows; row++)
            {
                sum += grid[row][col];
            }
            if (sum <= nrows / 2)
            {
                for (int row = 0; row < nrows; row++)
                {
                    grid[row][col] = !grid[row][col];
                }
            }
        }

        int r = 0;
        for (int row = 0; row < nrows; row++)
        {
            for (int col = 0; col < ncols; col++)
            {
                r += grid[row][col] * std::pow(2, (ncols - 1) - col);
            }
        }
        return r;
    }
};