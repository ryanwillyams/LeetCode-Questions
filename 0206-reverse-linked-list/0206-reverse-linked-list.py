# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return head
         
        ans = []
        while head != None:
            ans.append(head.val)
            head = head.next
        ans.reverse()
        newHead = ListNode(ans[0])
        newHeadRef = newHead
        for x in range(1,len(ans)) :
            newHead.next = ListNode(ans[x])
            newHead = newHead.next
        return newHeadRef         
