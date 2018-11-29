# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # method 3: 两个pointer，以不同的速度在遍历list，比如，行进速度分别为1，2，这样如果有cycle，早晚两个pointer都会相遇的！
        if not head: return False
        s1 = head
        s2 = head.next
        while s1 != s2:
            if not s2 or not s2.next:
                return False
            s1 = s1.next
            s2 = s2.next.next
        return True

        # method 2: 强行断开所有已访问过的节点，把他们的next设置为head（或随便一个统一的东西，以示其访问过）。
        # 接下来谁的next为head，谁就是访问过的节点！（若结点没被访问过，它的next会是一个正常的结点地址）
#         cur = head
#         while cur:
#             cur_next = cur.next
#             if cur_next == head:
#                 return True
#             cur.next = head
#             cur = cur_next
#         return False


# method 1: hash map:使用python的dict存储每个节点地址，如果下个节点在dict中存在过，则说明cycle。
# hashmap = {}
# while head:
#     if hashmap.__contains__(head.next):
#         return True
#     hashmap[head.next] = 0
#     head = head.next
# return False
