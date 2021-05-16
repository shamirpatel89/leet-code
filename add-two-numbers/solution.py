# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode()
        current_node = result_node
        sum = 0

        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            current_node.next = ListNode(sum % 10, None)

            current_node = current_node.next
            sum = sum // 10

        return result_node.next
