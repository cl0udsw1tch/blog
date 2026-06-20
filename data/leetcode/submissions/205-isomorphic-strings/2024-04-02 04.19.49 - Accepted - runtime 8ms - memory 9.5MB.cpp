class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> m, n;
        int size = s.size();
        if (size != t.size()) return false;

        
        for (int i = 0; i < size; i++)
        {
            if (!m[t[i]])
            {
                if (n[s[i]]) return false;
                m[t[i]] = s[i];
                n[s[i]] = '1';
            }
            else
            {
                if (m[t[i]] != s[i])
                {
                    return false;
                }
            }
            

        }
        return true;
    }
};