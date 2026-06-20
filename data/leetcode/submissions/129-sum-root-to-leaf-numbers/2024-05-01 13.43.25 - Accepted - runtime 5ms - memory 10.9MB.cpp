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

    private:
        int dfs(TreeNode* node, int curr)
        {
            if (!node)
            {
                return 0;
            }
            if (!node->left && !node->right)
            {
                return curr * 10 + node->val;
            }
            return dfs(node->left, curr * 10 + node->val) + dfs(node->right, curr * 10 + node->val); 
            
        }

public:


    int sumNumbers(TreeNode* root) {
        if (!root)
        {
            return 0;
        }
        if (!root->left && !root->right)
        {
            return root->val;
        }
        return dfs(root, 0.1);
    }
};