# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        else:
            return self.mergeKListsHelper(lists, 0, len(lists)-1)

    def mergeKListsHelper(self, lists, start, end):
        if start == end:
            return lists[start]
        
        if start + 1 == end:
            return self.mergeTwoLists(lists[start], lists[end])

        mid = start + (end - start) // 2
        left = self.mergeKListsHelper(lists, start, mid)
        right = self.mergeKListsHelper(lists, mid + 1, end)

        return self.mergeTwoLists(left, right)
        
    def mergeTwoLists(self, list1, list2):
        dummy = node = ListNode()
            
        while list1 and list2 :
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next