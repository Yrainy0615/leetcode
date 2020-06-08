"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""
"""
思路：需要考虑特殊情况
1：长度不相等  123+45657
2：存在进位 11+99=100
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers1(self, l1:ListNode, l2:ListNode)->ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        ->Listnode称为功能注释，表示该函数返回一个ListNode
        """
        head = ListNode(0)   #头结点，无存储，指向链表第一个结点
        node = head          #初始化链表结点
        carry = 0            #初始化 进一 标志位
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10 #0 or 1
            node.next = ListNode(sum % 10)  # 取余数，求本位结点
            if l1:        #若链表不空，则继续后移
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next   # 更新指针
        if carry != 0:  #验证最后一位相加是否需 进一
            node.next = ListNode(1)
        return head.next # 返回头结点的下一个结点，即链表的第一个结点

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
            prenode = ListNode(0)
            lastnode = prenode
            val = 0
            while val or l1 or l2:
                #divmod(a,b)返回（a//b,a%b）
                val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
                lastnode.next = ListNode(cur)
                lastnode = lastnode.next
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
            return prenode.next


#创建链表
def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

#打印链表
def printList(l: ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print('')

if __name__ == "__main__":
    l1 = generateList([1, 5, 8])
    l2 = generateList([9, 1, 2, 9])
    printList(l1)
    printList(l2)
    s = Solution()
    sum1 = s.addTwoNumbers1(l1, l2)
    sum2 = s.addTwoNumbers2(l1, l2)
    printList(sum1)
    printList(sum2)


