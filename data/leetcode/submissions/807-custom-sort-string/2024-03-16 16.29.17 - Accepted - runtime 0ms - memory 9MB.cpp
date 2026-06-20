class Solution {
public:
    void quickSort(string& s, const int& start, const int& end,     std::unordered_map<char, int>& order)
    {
        if (end == start)
        {
            return;
        }
        if (end == start + 1)
        {
            if (!order[s[start]] || !order[s[end]])
            {
                return;
            }
            if (order[s[start]] > order[s[end]])
            {
                char tmp = s[end];
                s[end] = s[start];
                s[start] = tmp;
            }
            return;
        }

        int pivotPos = end;
        while (!order[s[pivotPos]] && pivotPos > start)
        {
            pivotPos--;
        }
        if (pivotPos == start)
        {
            return;
        }

        char pivot = s[pivotPos];
        int queryPos = pivotPos - 1;
        while (queryPos > start - 1)
        {
            if (!order[s[queryPos]])
            {
                queryPos--;
                continue;
            }
            
            if (order[s[queryPos]] > order[pivot])
            {
                char beforePivot = s[pivotPos - 1];
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
            quickSort(s, start, pivotPos, order); // this gets the pivot
            quickSort(s, pivotPos + 1, end, order);
        }
        else
        {
            quickSort(s, start, pivotPos - 1, order); 
        }

    }
    string customSortString(string order, string s) {
        std::unordered_map<char, int> ordering;

        int i = 1;
        for (char& c : order)
        {
            ordering[c] = i++;
        }

        quickSort(s,0,s.size()-1, ordering);
        return s;

    }

};