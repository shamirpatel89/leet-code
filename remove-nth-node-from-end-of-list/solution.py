# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes: List[ListNode] = []

        current = head

        if not current.next:
            return None

        while current:
            nodes.append(current)
            current = current.next

        if n == len(nodes):
            return head.next

        index = n * -1
        previous = index - 1
        next = index + 1
        nodes[previous].next = nodes[index].next

        return head
