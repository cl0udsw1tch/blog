class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {

        int currLen = 0;
        int currCost = 0;
        int maxLen = 0;
        int slow = 0, fast = 0;
        bool ch;
        int cost;
        while (fast < s.size())
        {
            currCost+=std::abs(s[fast] - t[fast]);
            currLen++;
            ch = currCost <= maxCost;


            while (!ch && slow <= fast)
            {
                cost = std::abs(s[slow] - t[slow]);
                currCost-=cost;
                currLen--;
                ch = currCost <= maxCost;
                slow++;
            }
            maxLen = std::max(maxLen, currLen);
            fast++;
        }
        return maxLen;

    }
};