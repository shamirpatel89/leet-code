# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        current_node = result

        while l1 or l2:
            new_node = ListNode()
            min_val = 0
            if l1 and l2:
                if l1.val <= l2.val:
                    new_node.val = l1.val
                    l1 = l1.next
                else:
                    new_node.val = l2.val
                    l2 = l2.next
            elif l1:
                new_node.val = l1.val
                l1 = l1.next
            elif l2:
                new_node.val = l2.val
                l2 = l2.next

            current_node.next = new_node
            current_node = current_node.next

        return result.next
