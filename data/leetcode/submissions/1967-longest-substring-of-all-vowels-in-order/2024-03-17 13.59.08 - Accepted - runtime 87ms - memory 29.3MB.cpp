class Solution {
public:
    int longestBeautifulSubstring(string word) {
        // sliding window
        if (word.size() < 5)
        {
            return 0;
        }
        std::unordered_map<char, int> order;
        order['a'] = 1;
        order['e'] = 2;
        order['i'] = 3;
        order['o'] = 4;
        order['u'] = 5; 

        int maxLen = 0;
        int currLen = 0;
        char prev = '\0';

        int end_ptr = 0;
        while (word[end_ptr] != 'a' && end_ptr < word.size())
        {
            end_ptr++;
        }
        
        prev = 'a';
        while (end_ptr < word.size())
        {
            int start_ptr = end_ptr;
            while ((word[end_ptr] == prev || order[word[end_ptr]] == order[prev] + 1) 
            && end_ptr < word.size())
            {
                if (word[end_ptr] != prev)
                {
                    prev = word[end_ptr];
                }
                end_ptr++;
            }
            if (word[end_ptr - 1] == 'u')
            {
                currLen = end_ptr - start_ptr;
                maxLen = currLen > maxLen ? currLen : maxLen;
            }

            while (word[end_ptr] != 'a' && end_ptr < word.size())
            {
                end_ptr++;
            }
            currLen = 0;
            prev = 'a';
        }

        return maxLen;
    }
};