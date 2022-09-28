# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        res = 0
        
        cur = head
        while cur:
            cur = cur.next
            n +=1
        
        p = n-1
        
        while head:
            res += pow(2,p) * head.val
            p -=1
            head = head.next
            
        return res 