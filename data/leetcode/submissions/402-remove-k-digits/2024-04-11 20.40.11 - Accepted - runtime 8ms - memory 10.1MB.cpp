class Solution {
public:
    string removeKdigits(string num, int k) {
        string s;
        for (char c : num)
        {
            while (k && s.size() && s.back() > c)
            {
                s.pop_back();
                k--;
            }
            s+=c;
        }

        s=s.substr(0, s.size()- k);
        k--;
        

        auto first = std::find_if(s.begin(), s.end(), [](const char& first) -> bool {return first > '0';});
        int firstIdx = std::distance(s.begin(), first);
        s=s.substr(firstIdx);
        return s.size() ? s : "0";

    }
};