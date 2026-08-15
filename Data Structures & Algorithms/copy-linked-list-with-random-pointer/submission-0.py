"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 2 passes
        # Pass one i will save where each node goes and its info inside will be the val , next and random 
        mp = {}
        dummy = head
        while dummy:
            mp[dummy] = Node(dummy.val)
            dummy = dummy.next 
        # pass two will be create the head of the new and iterating through the hashtable 
        dummy = head
        while dummy:
            mp[dummy].next = mp.get(dummy.next)
            mp[dummy].random = mp.get(dummy.random)
            dummy = dummy.next
        return mp[head]
