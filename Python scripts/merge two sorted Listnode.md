## Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
```
Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

## Python

### iterative approach
```Python3
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_1 = l1
        node_2 = l2

        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val > l2.val:
            node_3 = ListNode(l2.val)
            node_2 = node_2.next
        else:
            node_3 = ListNode(l1.val)
            node_1 = node_1.next
        new_node = node_3
        while node_1 and node_2:
            if node_1.val > node_2.val:
                new_node.next = node_2
                node_2 = node_2.next
            else:
                new_node.next = node_1
                node_1 = node_1.next
            new_node = new_node.next
        if node_1:
            new_node.next = node_1
        if node_2:
            new_node.next = node_2
        return node_3
```
### Recursive approach
```
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```