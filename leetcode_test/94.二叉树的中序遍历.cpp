/*
 * @lc app=leetcode.cn id=94 lang=cpp
 *
 * [94] 二叉树的中序遍历
 */
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    };
#include <vector>
using namespace std;
// @lc code=start
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
    
    void zhongxu(TreeNode* root,vector<int>& res){
        if(root == nullptr) return;
        zhongxu(root->left,res);
        res.push_back(root->val);
        zhongxu(root->right,res);
    };
public:
    vector<int> inorderTraversal(TreeNode* root) {   vector<int> res;
        if(root == nullptr) return res;
        zhongxu(root,res);
        return res;
    }
};
// @lc code=end

