from typing import Optional, Union

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Union[ListNode, None] = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
        new_head = None
        temp_head = None
        for i in range(0, len(nodes) - 1, 2):
            nodes[i], nodes[i + 1], = nodes[i + 1], nodes[i]
        for ind, each_node in enumerate(nodes):
            if new_head is None:
                new_head = each_node
                temp_head = new_head
            else:
                temp_head.next = each_node
                temp_head = temp_head.next
                if ind == len(nodes) - 1:
                    temp_head.next = None
        return new_head

    def printList(self, head: Optional[ListNode]) -> None:
        while head is not None:
            print(head.val)
            head = head.next


if __name__ == '__main__':
    alist = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    sol = Solution()
    head = sol.swapPairs(alist)
    sol.printList(head)
