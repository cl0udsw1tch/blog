/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    int coinDistributer(TreeNode* root, int& numTrades)
    {
        if (!root->left && !root->right)
        {
            if (root->val > 1)
            {
                int temp = root->val;
                root->val = 1;
                numTrades+= temp - 1;
                return temp - 1;
            }
            else if (root->val == 1)
            {
                return 0;
            }
            return -1;
        }

        if (root->left)
        {
            int deltaLeft = coinDistributer(root->left, numTrades);
            if (deltaLeft < 0) numTrades += -1 * deltaLeft;
            root->val += deltaLeft;
            
        }
        if (root->right)
        {
            int deltaRight = coinDistributer(root->right, numTrades);
            if (deltaRight < 0) numTrades+= -1 * deltaRight;
            root->val += deltaRight;
        }

        int temp = root->val;
        root->val = 1;
        if (temp > 1)
        {
            numTrades+= temp - 1;
        }
        return temp - 1;
    }
    int distributeCoins(TreeNode* root) {
        int numTrades = 0;
        coinDistributer(root, numTrades);
        return numTrades;
    }
};