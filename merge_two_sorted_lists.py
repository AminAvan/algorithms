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
        current1 = list1
        current2 = list2
        sorted_linked_list = None
        # while current1 or current2:
        #     print(f"current1.val: {current1.val}")
        #     print(f"current2.val: {current2.val}")

        if (sorted_linked_list == None) and (current1.val <= current2.val):
            sorted_linked_list = ListNode(current1.val)
            current1 = current1.next
        if (sorted_linked_list == None) and (current2.val <= current1.val):
            sorted_linked_list = ListNode(current2.val)
            current2 = current2.next
        elif (sorted_linked_list != None) and (current1.val <= current2.val):
            sorted_linked_list.next = ListNode(current1.val)
            sorted_linked_list.val = ListNode(current1.val)
            current1 = current1.next
        elif (sorted_linked_list != None) and (current2.val <= current1.val):
            sorted_linked_list.next = ListNode(current2.val)
            sorted_linked_list.val = ListNode(current2.val)
            current2 = current2.next

        current = sorted_linked_list
        while current:
            print(f"current.val: {current.val}")
            current = current.next


            current1 = current1.next
            current2 = current2.next


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

    # current = merged_list
    # while current:
    #     print(f"current.val: {current.val}")
    #     print(f"current.next: {current.next}")
    #     current = current.next

    pass

# call the main function
if __name__ == "__main__":
    main()