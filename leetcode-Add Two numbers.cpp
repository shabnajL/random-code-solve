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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* new_var = new ListNode();
        ListNode* temp = new_var;
        int carry_sum = 0;
        while(l1!=0 || l2!=0 || carry_sum==1)
        {
            int sum = 0;
            
            if(l1!=0){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2!=0){
                sum += l2->val;
                l2 = l2->next;
            }
            //cout<<sum<<endl;
            sum += carry_sum;
            //cout<<sum<<endl;
            carry_sum = sum/10;
            sum = sum%10;
            //cout<<sum<<endl;
            ListNode* new_node = new ListNode(sum);
            temp->next = new_node;
            temp = temp->next;
            //cout<<temp->val<<endl;
        }
        return new_var->next;
    }
};
