class Solution {
public:
    string minRemoveToMakeValid(string s) {
        
        if (s.size() == 1)
        {
            if (s[0] != '(' && s[0] != ')')
            {
                return s;
            }
            else
            {
                return "";
            }
        }
        else
        {
            stack<int> st;
            int ptr = 0;
            while (ptr < s.size())
            {
                if (s[ptr] != '(' && s[ptr] != ')')
                {
                    ptr++; continue;
                }
                if (!st.size())
                {
                    st.push(ptr);
                    ptr++; continue;
                }

                if (s[ptr] == ')' && s[st.top()] == '(')
                {
                    st.pop(); ptr++;
                }
                else
                {
                    st.push(ptr); ptr++;
                }
            }

            if (!st.size()) return s;
            int first;
            int second = s.size();                                         
            string t;
            while (st.size())
            {
                first = st.top();
                st.pop();
                t = s.substr(first + 1, second - first) + t;
                second = first - 1;
            }
            if (second == -1) return t;
            return s.substr(0, first) + t;


        }


    }
};