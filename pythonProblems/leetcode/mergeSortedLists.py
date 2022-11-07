# Definition for singly-linked list.
from typing import List, Optional, Tuple, Union


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Union[ListNode, None] = next


class Solution:

    def __init__(self):
        self.lists = []

    def ret_node_value_and_next(self, index: int) -> Union[int, List]:
        val = self.lists[index].val if self.lists[index] is not None else None
        next = self.lists[index].next if self.lists[index] is not None else None
        if next:
            self.lists[index] = next
        else:
            self.lists[index] = None
        return val if val != None else []

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(self.lists) == 0:
            self.lists = lists
        nodes = []
        new_head = None
        loop = True
        while loop:
            result = [Solution.ret_node_value_and_next(
                self, ind) for ind in range(len(self.lists))]
            old_len = len(nodes)
            for eachValue in result:
                if eachValue != []:
                    nodes.append(eachValue)
            if len(nodes) == old_len:
                break
        nodes.sort()
        tmp_head = None
        for eachNodeValue in nodes:
            if new_head is None:
                new_head = ListNode(eachNodeValue)
                tmp_head = new_head
            elif tmp_head is not None:
                tmp_head.next = ListNode(eachNodeValue)
                tmp_head = tmp_head.next
        return new_head

    # def print_list(self, head: Union[ListNode, None]) -> None:
    #     while head is not None:
    #         print(head.val)
    #         if head.next:
    #             head = head.next
    #         else:
    #             break
    #     print('Done!')


if __name__ == '__main__':
    first_list = ListNode(0, ListNode(2, ListNode(5)))
    # second_list = ListNode(1, ListNode(3, ListNode(4)))
    # third_link = ListNode(2, ListNode(6))

    sol = Solution()
    new_head = sol.mergeKLists([first_list])
    sol.print_list(new_head)
