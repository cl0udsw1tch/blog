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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1)
        {
            TreeNode* newRoot = new TreeNode(val);
            newRoot->left = root;
            return newRoot;
        }
        if (depth == 2)
        {
            TreeNode* newLeft = new TreeNode(val), *newRight = new TreeNode(val);
            newLeft->left = root->left;
            newRight->right = root->right;
            root->left = newLeft;
            root->right = newRight;
            return root;
        }

        root->left = root->left ? addOneRow(root->left, val, depth - 1) : nullptr;
        root->right = root->right ? addOneRow(root->right, val, depth - 1) : nullptr;
        return root;

    }
};