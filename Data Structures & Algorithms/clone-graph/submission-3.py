"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}
        def dfs(root):
            if not root:
                return
            if root.val in mp:
                return mp[root.val]
            newNode = Node(root.val)
            mp[root.val] = newNode
            for neighbor in root.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)

