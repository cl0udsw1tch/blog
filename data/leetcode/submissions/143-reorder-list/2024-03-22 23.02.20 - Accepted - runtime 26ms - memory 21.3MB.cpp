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
    void reorderList(ListNode* head) {
        ListNode* slow = head, *fast = head;
        if (!head || !head->next || !head->next->next)
        {
            return ;
        }
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next = head->next;
        while (fast->next && fast->next->next)
        {
            slow=slow->next;
            fast = fast->next->next;
            curr->next = prev;
            prev=curr;
            curr=next;
            next=next->next;
            
        }
        ListNode* right = slow->next;
        
        ListNode* right_next = right->next;
        curr->next=prev;


        ListNode* left = nullptr;
        ListNode* left_back = curr;
        if (!fast->next)
        {
            left=curr;
            left->next=nullptr;
            left_back = prev;
        }
        while(left_back)
        {
            ListNode* tmp = left_back->next, *tmp2 = right_next ? right_next->next : nullptr;
            
            right->next = left;
            left_back->next = right;

            left=left_back;
            left_back=tmp;

            right=right_next;
            right_next = tmp2;
        }

    }
};