# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        curr = res

        while True:
            minNode = -1

            for i in range(len(lists)):
                if not Lists[i]:
                    continue
                if minNode == -1 or Lists[i].val < Lists[minNode].val:
                    minNode = i

            if minNode == -1:
                break
            curr.next = Lists[minNode]
            curr = curr.next
            Lists[minNode] = Lists[minNode].next

        curr.next = None
        return res.next

