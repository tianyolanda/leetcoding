# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # method 2: 两个pointer，分按照A->B,B->A 这样的路线走，如果有重叠，则他们会遇上。如果没有重叠，俩pointer都会走到底。

        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa

        # method 1:
        # hashmap={}
        # while headA:
        #     hashmap[headA]=0
        #     headA = headA.next
        # while headB:
        #     if hashmap.__contains__(headB):
        #         return headB
        #     headB = headB.next
        # return None

