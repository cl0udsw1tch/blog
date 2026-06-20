class Solution {
public:
    bool checkValidString(string s) {
        if (s.empty()) return true;
    
    stack<int> leftParStack, starStack;
    
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '(') {
            leftParStack.push(i);
        } else if (s[i] == '*') {
            starStack.push(i);
        } else { // ')' encountered
            if (!leftParStack.empty()) {
                leftParStack.pop(); // Match '('
            } else if (!starStack.empty()) {
                starStack.pop(); // Use '*' as '('
            } else {
                return false; // No matching '(' or '*' found
            }
        }
    }
    
    // Now we have unmatched '(' and '*' in their respective stacks.
    while (!leftParStack.empty() && !starStack.empty()) {
        if (leftParStack.top() > starStack.top()) {
            return false; // '*' appears before '('
        }
        leftParStack.pop();
        starStack.pop();
    }
    
    return leftParStack.empty();
    }
};