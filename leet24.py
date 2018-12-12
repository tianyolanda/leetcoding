class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = head
        count = 0
        front = head
        while front:
            if not front.next:
                new = front
                return new
            else:
                new = front.next
                new.next = front
                front = front.next.next
                new = new.next.next

        # new = head
        return new

head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(5)

head1.next = head2
head2.next = head3
# head3.next = head4
# head4.next = head5
print(head1,head2)
head1,head2 = head2,head1
print(head1.next,head1.val,head2.next,head2.val)
# so = Solution()
# so.swapPairs(head1)