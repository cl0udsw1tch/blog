class Solution {
public:
    int maximumLengthSubstring(string s) {
        
        int maxLen = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            std::map<char, int> counts;
            int currLen=0;
            for (int j = 0; j < s.size() - i; j++)
            {
                if (counts[s[i + j]] == 2)
                {
                    break;
                }
                counts[s[i+j]]++;
                currLen++;    
            }
            
            if (currLen > maxLen) maxLen = currLen;
        }
        return maxLen;
    }
};