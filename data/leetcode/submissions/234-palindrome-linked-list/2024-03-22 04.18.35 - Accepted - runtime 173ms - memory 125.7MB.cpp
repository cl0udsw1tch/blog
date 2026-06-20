/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next)
        {
            return true;
        }
        ListNode* slow = head, *fast = head;
        std::vector<int> stack;
        stack.push_back(head->val);
        while (fast->next && fast->next->next)
        {
            slow=slow->next;
            fast=fast->next->next;
            stack.push_back(slow->val);
        }
        ListNode* rightStart = nullptr;
        if (fast->next)
        {
            rightStart = slow->next;
        }
        else
        {
            rightStart = slow;
        }
        while (rightStart)
        {
            if (!stack.size())
            {
                return false;
            }
            int val = stack[stack.size() - 1];
            if (rightStart->val != val)
            {
                return false;
            }
            stack.pop_back();
            rightStart=rightStart->next;
        }
        return true;
    }
};