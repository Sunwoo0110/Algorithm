# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    
        return dfs(root, float('-inf'), float('inf'))

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ## 배열 인덱스로 받는 경우 -> 트리로 변환하기
# def build_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
#     if not arr:
#         return None
    
#     # 값이 None이 아니면 노드 생성, None이면 빈 자리
#     nodes = [TreeNode(v) if v is not None else None for v in arr]
#     n = len(arr)
    
#     for i in range(n):
#         if nodes[i] is None:
#             continue
        
#         left_idx = 2*i+1
#         right_idx = 2*i+2
        
#         if left_idx < n:
#             nodes[i].left = nodes[left_idx]
#         if right_idx < n:
#             nodes[i].right = nodes[right_idx]
    
#     return nodes[0]

# ## BST 판별 (DFS + 범위 전달)
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
#             if node is None:
#                 return True
            
#             if not (low < node.val < high):
#                 return False
            
#             return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
#         return dfs(root, float('-inf'), float('inf'))
