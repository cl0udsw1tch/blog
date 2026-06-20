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
    ListNode* removeZeroSumSublists(ListNode* head) {
        
        // base
        if (head == nullptr)
        {
            return head;
        }
        if (head->next == nullptr)
        {
            if (head->val == 0)
            {
                return nullptr;
            }
            return head;
        }

        int sum = head->val;
        ListNode* curr = head->next;
        while (sum != 0 && curr)
        {
            sum+=curr->val;
            curr=curr->next;
        }
        if (sum == 0)
        {
            head = removeZeroSumSublists(curr);
        }
        else
        {
            head->next = removeZeroSumSublists(head->next);
        }
        return head;

    }
};