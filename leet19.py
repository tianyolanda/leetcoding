# 方法一：两次遍历
# 1. 遍历整个list，记录长度
# 2. 遍历找到第（长度-n）个节点，删掉节点

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
        count = 1
        head_now = head

        while head_now.next != None:
            head_now = head_now.next
            count += 1

        print('删除倒数第',n,'个结点')
        head_past = head
        head_now = head

        if n == count:
            head = head.next
            return head


        for i in range(count-n+1):
            if i == count-n:
                head_past.next = head_now.next
                return head
            head_past = head_now
            head_now = head_now.next




head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(3)
head4 = ListNode(4)
head5 = ListNode(5)

head1.next = head2
head2.next = head3
head3.next = head4
head4.next = head5

so = Solution()
head1.printlist()
# so2 = Solution()
list2 = so.removeNthFromEnd(head1,2)
list2.printlist()