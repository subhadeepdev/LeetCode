import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index))

        if not heap:
            return None
        val, index = heapq.heappop(heap)
        mergedList = lists[index]
        lists[index] = lists[index].next
        if lists[index]:
            heapq.heappush(heap, (lists[index].val, index))

        currentNode = mergedList
        while heap:
            val, index = heapq.heappop(heap)
            currentNode.next = lists[index]
            currentNode = currentNode.next

            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))

        currentNode.next = None
        return mergedList
        
print(Solution().mergeKLists([[1,4,5],[1,3,4],[2,6]]))