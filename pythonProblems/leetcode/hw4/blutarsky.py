from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    name: str
    rating: int
    parent: Node = None
    left_child: Node = None
    right_sib: Node = None


def get_guest_list(root: Node, table: dict | None = None) -> tuple[list[Node], int]:
    # If DP table not yet initialized, initialize DP table
    if table is None:
        table = {}

    if root == None:
        # if root is None, return an empty guest list and a rating of 0
        return [], 0
    elif root.name in table:
        # if the best guest list for this root has been calculated already, return it
        return table[root.name]

    # Assume best guest list include the root, so start with the root's info
    guests = [root]
    ratings = root.rating

    # Check the best guest lists of the child nodes, which can't necessarily be used in
    # a list containing the root due to the root being an immediate superior
    child_guests, child_ratings = get_guest_list(root.left_child, table)

    # The siblings CAN be used with the root node, as there is no supervisor/employee
    # relationship to account for
    sibling_guests, sibling_ratings = get_guest_list(root.right_sib, table)

    # Get best lists of grandchildren nodes, wherever possible, as they aren't immediate
    # employees of the root supervisor
    root_child = root.left_child
    while root_child != None:
        if root_child.left_child != None:
            grandchild_guests, grandchild_ratings = get_guest_list(
                root_child.left_child, table)
            guests += grandchild_guests
            ratings += grandchild_ratings

        root_child = root_child.right_sib

    # We can include sibling lists with our root and children lists, since the direct sibling of
    # the root has no significant relationship with either
    # guests += sibling_guests
    # ratings += sibling_ratings
    # child_guests += sibling_guests
    # child_ratings += sibling_ratings

    # For this root, choose the rating-maximized list, which is either the list that contains
    # this node, or the list that includes the children of this node
    if child_ratings > ratings:
        if root.name not in table:
            table[root.name] = (child_guests + sibling_guests,
                                child_ratings+sibling_ratings)
        return child_guests + sibling_guests, child_ratings+sibling_ratings
    else:
        if root.name not in table:
            table[root.name] = (guests + sibling_guests,
                                ratings+sibling_ratings)
        return guests + sibling_guests, ratings+sibling_ratings


computed_nodes: dict = {}
list_sums = {}


def get_guest_list_v2(node: Node | None, level: int = 0) -> int:
    if node == None:
        return 0
    # grandchildren sum vs child sums
    # first compute grandchild sums + grandchild right sums, then compute children sums
    max_sum = node.rating
    if node.left_child is not None:  # GRANDCHILDREN SUM
        # if it has a left child, access it's grandchildren sum
        max_sum += get_guest_list_v2(
            node.left_child.left_child, level + 2)
    if node.left_child is not None:  # gather grandchild sums from left child
        max_sum = max(max_sum, get_guest_list_v2(node.left_child, level + 1))
    if node.right_sib:  # RIGHT CHILD SUM
        # if it doesn't have a grandchild, access it's right sib sum, that sums up the grandchild sum of the right children
        max_sum = get_guest_list_v2(node.right_sib, level)
    print(node.name)
    print(level, max_sum)
    return max_sum


def print_guest_list(guests: list[Node]) -> None:
    print(f"TOTAL RATING: {sum(guest.rating for guest in guests)}")
    print("GUESTS:")
    for guest in guests:
        print(guest.name, guest.rating)


if __name__ == "__main__":

    # ####################### MAKE FIRST TESTING TREE #######################
    # root_1 = Node("A", 10)

    # for i in range(3):
    #     name = chr(ord("B")+i)
    #     lvl_1 = Node(name, 2+i, parent=root_1)

    #     grand2 = Node(name+"2", 1, parent=lvl_1)
    #     grand1 = Node(name+"1", 1, parent=lvl_1, right_sib=grand2)

    #     great_grand1 = Node(name+"11", 1, parent=grand1)
    #     great_grand2 = Node(name+"22", 1, parent=grand2)

    #     grand1.left_child = great_grand1
    #     grand2.left_child = great_grand2

    #     lvl_1.left_child = grand1

    #     if root_1.left_child == None:
    #         root_1.left_child = lvl_1
    #     else:
    #         level = root_1.left_child
    #         while level.right_sib != None:
    #             level = level.right_sib

    #         level.right_sib = lvl_1

    ####################### MAKE SECOND TESTING TREE #######################
    root_2 = Node("A", 1)

    for i in range(3):
        name = chr(ord("B")+i)
        lvl_1 = Node(name, 5+i, parent=root_2)  # C

        val = 10 if i % 2 == 0 else 1
        grand2 = Node(name+"2", val, parent=lvl_1)  # C2
        grand1 = Node(name+"1", val, parent=lvl_1, right_sib=grand2)  # C1

        great_grand1 = Node(name+"11", 1, parent=grand1)  # C11
        great_grand2 = Node(name+"22", 1, parent=grand2)  # C22

        grand1.left_child = great_grand1
        grand2.left_child = great_grand2

        lvl_1.left_child = grand1

        if root_2.left_child == None:
            root_2.left_child = lvl_1
        else:
            level = root_2.left_child
            while level.right_sib != None:
                level = level.right_sib

            level.right_sib = lvl_1

        #print(great_grand1.name, great_grand1.right_sib)

    guests, ratings = get_guest_list_v2(root_2)
    print(ratings)
    print_guest_list(guests)
