/*
 * @lc app=leetcode.cn id=21 lang=cpp
 *
 * [21] 合并两个有序链表
 */
#include <list>
#include <algorithm>
using namespace std;
struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
};
// @lc code=start
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* p=new ListNode();
        ListNode* head=p;
        if(list1==nullptr){
            return list2;
        }
        if(list2==nullptr){
            return list1;
        }
        ListNode *p1=list1,*p2=list2;
        while(p1!=nullptr&&p2!=nullptr){
            if(p1->val<p2->val){
                p->next=p1;
                p1=p1->next;
            }
            else{
                p->next=p2;
                p2=p2->next;
            }
            p=p->next;
        }
        if(p1!=nullptr){
            p->next=p1;
        }
        if(p2!=nullptr){
            p->next=p2;
        }
        return head->next;
    }
    
};
// @lc code=end

