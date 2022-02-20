class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(5, ListNode(6, ListNode(4, None)))
l2 = ListNode(2, ListNode(4, ListNode(3, None)))


class Solution:

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        l3 = []
        n = l1
        m = l2
        while n is not None:
            l3.append(n.val + m.val)
            n = n.next


x = Solution.addTwoNumbers(l1, l2)
