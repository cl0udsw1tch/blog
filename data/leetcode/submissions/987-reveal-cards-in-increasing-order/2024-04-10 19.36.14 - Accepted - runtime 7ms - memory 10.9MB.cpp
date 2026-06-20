class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        std::sort(deck.begin(), deck.end(), std::greater<int>());
        vector<int> r;
        for (int num : deck)
        {
            if (r.size() > 1)
            {
                std::rotate(r.begin(), r.begin() + 1, r.end());
            }
            r.push_back(num);
        }
        std::reverse(r.begin(), r.end());
        return r;
        
    }
};