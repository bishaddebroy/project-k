# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)
    
    def divide(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left > right:
            return None
        if left == right:
            return lists[left]
        
        mid = left + (right - left) // 2
        left_half = self.divide(lists, left, mid)
        right_half = self.divide(lists, mid + 1, right)
        
        return self.conquer(left_half, right_half)
    
    def conquer(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2
        return dummy.next
    
