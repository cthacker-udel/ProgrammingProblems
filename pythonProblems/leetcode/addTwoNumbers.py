from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        l3 = None
        carry = 0
        calculated_value = 0
        while l1 != None or l2 != None:
            val_1 = l1.val if l1 != None else 0
            val_2 = l2.val if l2 != None else 0
            the_sum = val_1 + val_2
            if (the_sum + carry) >= 10:
                calculated_value = (
                    the_sum + 1) % 10 if carry > 0 else the_sum % 10
                carry = 1
            else:
                if carry > 0:
                    calculated_value = the_sum + carry
                    carry = 0
                else:
                    calculated_value = the_sum

            new_node.next = ListNode() if ((l1 != None) or (l2 != None)) and l3 != None else None
            new_node = new_node.next if (
                (l1 != None) or (l2 != None)) and l3 != None else new_node
            new_node.val = calculated_value
            if l3 == None:
                l3 = new_node

            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        if carry > 0:
            new_node.next = ListNode(carry)
        # while l3 != None:
        #     print(l3.val)
        #     l3 = l3.next
        return l3


if __name__ == '__main__':
    l1 = ListNode()
    l1.val = 9
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode()
    l2.val = 9
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    sol = Solution()
    sol.addTwoNumbers(l1, l2)
