class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode(0)

    def get(self, index: int) -> int:
        node = self.dummy
        i = -1
        while node and i < index:
            node = node.next
            i += 1
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        if self.dummy.next:
            new_head.next = self.dummy.next
            self.dummy.next = new_head
        else:
            self.dummy.next = new_head

    def addAtTail(self, val: int) -> None:
        node = self.dummy
        while node.next:
            node = node.next
        node.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        prev = self.dummy
        i = 0
        while prev.next and i < index:
            prev = prev.next
            i += 1
        if i < index:
            return
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        prev = self.dummy
        i = 0
        while prev and i < index:
            prev = prev.next
            i += 1
        if not prev:
            return
        prev.next = prev.next.next if prev.next else None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
