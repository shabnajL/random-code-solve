### LeetCode 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        len_head = 0
        while current is not None:
            current = current.next
            len_head = len_head + 1
        middle = (len_head // 2)
        # print(middle)
        output_list = head
        while middle>0:
            output_list = output_list.next
            middle -= 1
        return output_list
        
