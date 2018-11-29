# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = []
        for i in lists:
            while i:
                vals += [i.val]
                i = i.next
        vals.sort()
        return vals