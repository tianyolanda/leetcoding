# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwoLists(l1, l2):
            helpNode = ListNode(-99)
            cur = helpNode
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                    cur = cur.next
                else:
                    cur.next = l1
                    l1 = l1.next
                    cur = cur.next
            if l1 is None:
                cur.next = l2
            if l2 is None:
                cur.next = l1
            head = helpNode.next
            del helpNode
            return head

        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]

        res = lists[0]
        for i in lists[1:]:
            res = mergeTwoLists(i, res)
        return res