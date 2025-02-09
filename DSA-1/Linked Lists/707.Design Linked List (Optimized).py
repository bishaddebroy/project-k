# https://leetcode.com/problems/design-linked-list/

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def getPrev(self, index: int) -> int:
        if index <= self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        
        else:
            curr = self.tail
            for _ in range(self.size - index + 1):
                curr = curr.prev

        return curr


    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val
        

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = ListNode(val)
        prev = self.getPrev(index)
        next = prev.next
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.getPrev(index)
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)