# 方法二：一次遍历(beat 99.28%)
# 定义两个point：first和second，距离相差n
# first往前走，second也往前走，这样当first到达尽头的时候，second就是(length-n)，直接将second指向的节点删除

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
        first = head
        second = head

        for i in range(n):
            if first.next == None:
                return head.next
            first = first.next

        while first.next != None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head

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
list2 = so.removeNthFromEnd(head1,2)
list2.printlist()