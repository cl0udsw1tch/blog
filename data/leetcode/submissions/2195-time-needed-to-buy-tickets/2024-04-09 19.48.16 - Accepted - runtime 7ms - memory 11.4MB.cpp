class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int t = 0;
        queue<pair<int, int>> q;
        for (int i = 0; i < tickets.size(); i++)
        {
            q.push({i, tickets[i]});
        }
        pair<int, int> curr;
        while (true)
        {
            curr = q.front();
            q.pop();
            t++;
            curr.second--;
            if (curr.second)
            {
                q.push(curr);
            }
            else
            {
                if (curr.first == k)
                {
                    return t;
                }
                else
                {
                    continue;
                }
            }
        }
        return -1;
    }
};