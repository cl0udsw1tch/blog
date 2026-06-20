class Solution {
public:
    void quickSort(vector<vector<int>>& s, const int& start, const int& end)
    {
        if (end == start)
        {
            return;
        }
        if (end == start + 1)
        {
            if (s[start][0] > s[end][0])
            {
                vector<int> tmp = s[end];
                s[end] = s[start];
                s[start] = tmp;
            }
            return;
        }

        int pivotPos = end;

        vector<int> pivot = s[pivotPos];
        int queryPos = pivotPos - 1;
        while (queryPos > start - 1)
        {
            
            if (s[queryPos][0] > pivot[0])
            {
                vector<int> beforePivot = s[pivotPos - 1];
                s[pivotPos] = s[queryPos];
                s[pivotPos - 1] = pivot;
                if (queryPos < pivotPos - 1)
                {
                    s[queryPos] = beforePivot;
                }
                queryPos--;
                pivotPos--;
            }
            else
            {
                queryPos--;
                continue;
            }
        }

        if (pivotPos != end)
        {
            quickSort(s, start, pivotPos); // this gets the pivot
            quickSort(s, pivotPos + 1, end);
        }
        else
        {
            quickSort(s, start, pivotPos - 1); 
        }

    }
    int findMinArrowShots(vector<vector<int>>& points) {
        quickSort(points, 0, points.size() -1);

        int currBalloon = 0;
        int numShots = 0;
        while (currBalloon < points.size())
        {
            if (currBalloon == points.size() - 1)
            {
                numShots++;
                break;
            }
           int numToUnpopped = 1;
           int end = points[currBalloon][1];
            while (currBalloon + numToUnpopped< points.size())
            {
                if (points[currBalloon + numToUnpopped][0] <= end)
                {
                    end = min(points[currBalloon + numToUnpopped][1], end);
                    numToUnpopped++;
                }
                else
                {
                    break;
                }
            }
            numShots++;
            currBalloon += numToUnpopped;
        }
        return numShots;
    }
};