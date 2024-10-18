"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1, list2)

def main():
    # create first linked list
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)

    # create second linked list
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = ListNode(6)

    # create an instance of the Solution class
    solution = Solution()

    merged_list = solution.mergeTwoLists(list1, list2)

    current = merged_list
    while current:
        print(f"current.val: {current.val}")
        print(f"current.next: {current.next}")
        current = current.next

    pass

# call the main function
if __name__ == "__main__":
    main()