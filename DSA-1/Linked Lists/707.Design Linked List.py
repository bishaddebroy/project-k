# https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.head, self.head.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.tail.prev, self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, prev, next = ListNode(val), curr.prev, curr
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

        
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            prev, next = curr.prev, curr.next
            prev.next = next
            next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)