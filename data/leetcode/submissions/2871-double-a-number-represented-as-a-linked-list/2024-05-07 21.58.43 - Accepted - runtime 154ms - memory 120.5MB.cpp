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

    ListNode* reverse(ListNode* head)
    {
        if (!head->next) return head;
        auto prev = head;
        auto curr = head->next;
        prev->next=nullptr;
        ListNode* next;
        while (curr)
        {
            next = curr->next;
            curr->next = prev;
            
            prev = curr;
            curr = next;
        }
        return prev;
    }
    ListNode* doubleIt(ListNode* head) {

        auto tail = reverse(head);
        auto curr = new ListNode();
        curr->next = tail;
        int currSum;
        int s;
        int carry = 0;
        while (curr->next)
        {
            currSum = curr->next->val * 2 + carry;
            s = currSum > 9 ? currSum - 10 : currSum;
            carry = currSum != s;
            curr->next->val = s;
            curr = curr->next;
        }
        if (carry)
        {
            curr->next = new ListNode(carry);
        }
        head = reverse(tail);
        return head;
        
    }

    
};