class Solution {
public:
    int maxDepth(string s) {
        if (s == "")
        {
            return 0;
        }
        if (s.size() == 1)
        {
            return 0;
        }
        else
        {
            stack<char> _stack;
            int d = 0;
            for (int i = 0; i < s.size(); i++)
            {
                if (s[i] != '(' && s[i] != ')') continue;
                if (!_stack.size())
                {
                    _stack.push(s[i]);
                    continue;
                }
                if ((_stack.top() == '(' && s[i] == ')' )
                || (_stack.top() == ')' && s[i] == '('))
                {
                    d = max((int)_stack.size(), d);
                    _stack.pop();
                }
                else
                {
                    _stack.push(s[i]);
                }
            }
            return d;
        }
    }
};