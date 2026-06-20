class Solution {
public:
    using Idx2d = pair<int, int>;
    using board_t = vector<vector<char>>;
    vector<Idx2d> getUnseenNeighbors(int nrows, int ncols, int row, int col, map<Idx2d, bool>& seen)
    {
        vector<Idx2d> neighbors;
        vector<int> rs = {row}, cs = {col};

        if (row < nrows - 1)
        {
            rs.push_back(row + 1);
        }
        
        if (col < ncols - 1)
        {
            cs.push_back(col + 1);
        }

        if (row > 0)
        {
            rs.push_back(row - 1);
        }
        
        if (col > 0)
        {
            cs.push_back(col - 1);
        }

        for (int r : rs)
        {
            for (int c : cs)
            {
                if (r == row && c == col)
                {
                    continue;
                }
                if (seen[make_pair(r, c)])
                {
                    continue;
                }
                if (r == row || c == col)
                {
                    neighbors.push_back(make_pair(r, c));
                }
                    
            }
        }
        return neighbors;
    }

    bool neighborIsNextChar(
        int nrows, 
        int ncols, 
        const Idx2d& currPos,
        const int& nextCharIdx, 
        const board_t& board, 
        const string& word,
        map<Idx2d, bool>& seen
        )
    {
        if (nextCharIdx == word.size()) return true;
        vector<Idx2d> neighbors = getUnseenNeighbors(nrows, ncols, currPos.first, currPos.second, seen);
        if (!neighbors.size()) return false;

        
        for (Idx2d idx : neighbors)
        {
            if (board[idx.first][idx.second] == word[nextCharIdx])
            {
                seen[idx] = true;
                if (!neighborIsNextChar(nrows, ncols, idx, nextCharIdx+1, board, word, seen))
                {
                    seen[idx] = false;
                    continue;
                }
                else
                {
                    
                    return true;
                }

            }
        } 
        return false;
    }

    bool findChar(const char& c, const board_t& board)
    {
        for (int row = 0; row < board.size(); row++)
        {
            for (int col = 0; col < board[0].size(); col++)
            {
                if (board[row][col] == c)
                {
                    return true;
                }
            }
        }
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {

        for (char c : word)
        {
            if (!findChar(c, board)) return false;
        }

        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        int nrows = board.size(), ncols = board[0].size();
        
        map<Idx2d, bool> seen; 
        for (int row = 0; row < nrows; row++)
        {
            for (int col = 0; col < ncols; col++)
            {
                if(board[row][col] == word[0])
                {
                    seen[make_pair(row, col)] = true;
                    if (!neighborIsNextChar(nrows, ncols, {row, col}, 1, board, word, seen))
                    {
                        seen[make_pair(row, col)] = false;
                        continue;
                    }
                    else
                    {
                        return true;
                    }
                }
            }
        }
        return false;

    }

    
};