# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        if l1 is None and l2 is None: return None

        # lbase,linner = (l1,l2) if l1.val > l2.val else (l2,l1)
        headnew = ListNode(-99)
        lnew = headnew

        while l1 and l2:
            if l1.val < l2.val:
                lnew = l1
                l1 = l1.next
                lnew = lnew.next
            else:
                lnew = l2
                l2 = l2.next
                lnew = lnew.next

        while l1:
            lnew.next = l1

        while l2:
            lnew.next = l2

        head = headnew.next
        del headnew
        return head

head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(5)

head1.next = head2
# head2.next = head3
head3.next = head4
head4.next = head5

so = Solution()
so.mergeTwoLists(head1,head3)