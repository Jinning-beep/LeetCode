# Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
```
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

```
**Note:**

Given n will always be valid.

**Follow up:**

Could you do this in one pass?

# Python3
```Python3
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        index = length - n
        if index == 0:
            return head.next
        current = head
        for i in range(1,index):
            current = current.next
        current.next = current.next.next
        return head
```