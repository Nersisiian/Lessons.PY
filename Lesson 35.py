# --------------------------------------------------------------------------

# def num_islands(grid):
#     if not grid:
#         return 0

#     rows, cols = len(grid), len(grid[0])
#     visited = [[False]*cols for _ in range(rows)]

#     def dfs(r, c):
#         if r < 0 or r >= rows or c < 0 or c >= cols:
#             return
#         if grid[r][c] == 0 or visited[r][c]:
#             return
#         visited[r][c] = True
#         dfs(r+1, c)
#         dfs(r-1, c)
#         dfs(r, c+1)
#         dfs(r, c-1)

#     count = 0
#     for r in range(rows):
#         for c in range(cols):
#             if grid[r][c] == 1 and not visited[r][c]:
#                 dfs(r, c)
#                 count += 1
#     return count

# grid = [
#     [1,0,0,1,1,1,0,0],
#     [1,0,0,0,0,0,0,0],
#     [0,0,0,1,1,0,1,0],
#     [0,1,0,0,0,0,1,0],
#     [1,1,1,0,0,0,1,0]
# ]

# print(num_islands(grid))  

# --------------------------------------------------------------------------    

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         prefix = strs[0]

#         for s in strs[1:]:
            
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""

#         return prefix

# --------------------------------------------------------------------------

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
#         return i == len(s)

# --------------------------------------------------------------------------

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         left = 0
#         curr_sum = 0
#         ans = float('inf')

#         for right in range(len(nums)):
#             curr_sum += nums[right]

#             while curr_sum >= target:
#                 ans = min(ans, right - left + 1)
#                 curr_sum -= nums[left]
#                 left += 1

#--------------------------------------------------------------------------

        