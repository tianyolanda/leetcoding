# 方法二：一次遍历(beat )
# 利用python的自带list方法，直接将原list存储到新list，然后返回list[-n]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printlist(self):
        now = self
        printstr = ''
        while now.next != None:
            printstr += str(now.val)
            printstr += "->"
            # print(self.val,"->")
            now = now.next
        printstr += str(now.val)
        print(printstr)


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list_ = []
        while head:
            list_ += [head.val]
            head = head.next

        del list_[-n]
        return list_


head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(5)

head1.next = head2
# head2.next = head3
# head3.next = head4
# head4.next = head5

so = Solution()
head1.printlist()
# so2 = Solution()
list2 = so.removeNthFromEnd(head1, 2)
# list2.printlist()