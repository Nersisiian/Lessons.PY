# ------------------------------------------------------------------- LeetCode Problem: 1929. Concatenation of Array

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums

# ------------------------------------------------------------------- LeetCode Problem: 1470. Shuffle the Array

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         ans = []
#         for i in range(n):
#             ans.append(nums[i])
#             ans.append(nums[i + n])
#         return ans

# ------------------------------------------------------------------- LeetCode Problem: 485. Max Consecutive Ones

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_count = 0
#         current = 0

#         for num in nums:
#             if num == 1:
#                 current += 1
#                 if current > max_count:
#                     max_count = current
#             else:
#                 current = 0

#         return max_count

# ------------------------------------------------------------------- LeetCode Problem: 1365. How Many Numbers Are Smaller Than the Current Number

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         sorted_nums = sorted(nums)
#         rank = {}
        
#         for i, num in enumerate(sorted_nums):
#             if num not in rank:
#                 rank[num] = i
        
#         return [rank[num] for num in nums]

# ------------------------------------------------------------------- 