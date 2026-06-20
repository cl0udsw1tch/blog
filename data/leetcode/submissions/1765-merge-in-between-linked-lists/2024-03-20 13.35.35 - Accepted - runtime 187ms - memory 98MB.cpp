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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        
        int i = 0;
        ListNode* startNode = list1;
        while (i < a - 1)
        {
            i++;
            startNode=startNode->next;
        }
        ListNode* endNode = startNode;
        while (i < b + 1)
        {
            i++;
            endNode = endNode->next;
        }

        ListNode* list2End = list2;
        while (list2End->next)
        {
            i++;
            list2End=list2End->next;
        }
        startNode->next = list2;
        list2End->next = endNode;
        return list1;
    }
};