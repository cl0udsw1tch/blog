class Solution {
public:
    string reversePrefix(string word, char ch) {
        auto instance = find(word.begin(), word.end(), ch);
        if (instance == word.end())
        {
            return word;
        }
        reverse(word.begin(), instance + 1);
        return word;

    }
};