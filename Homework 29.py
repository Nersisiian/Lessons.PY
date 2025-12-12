# -------------------------------------------------------------------------- LeetCode Problem 1: Two Sum

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}  

#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in seen:
#                 return [seen[diff], i]
#             seen[num] = i

# --------------------------------------------------------------------------  LeetCode Problem 9: Palindrome Number 

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False

#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10

#         return x == reversed_half or x == reversed_half // 10  
    
# --------------------------------------------------------------------------  LeetCode Problem 13: Roman to Integer

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         values = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         total = 0

#         for i in range(len(s)):
            
#             if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
#                 total -= values[s[i]]
#             else:
#                 total += values[s[i]]

#         return total

# -------------------------------------------------------------------------- LeetCode Problem 14: Longest Common Prefix

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

# -------------------------------------------------------------------------- LeetCode Problem 20: Valid Parentheses

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         pairs = {
#             ')': '(',
#             ']': '[',
#             '}': '{'
#         }

#         for ch in s:
            
#             if ch in "([{":
#                 stack.append(ch)
#             else:
                
#                 if not stack or stack[-1] != pairs[ch]:
#                     return False
#                 stack.pop()

#         return len(stack) == 0

# -------------------------------------------------------------------------- LeetCode Problem 26: Remove Duplicates from Sorted Array

# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
    
#         k = 1
#         for i in range(1, len(nums)):
            
#             if nums[i] != nums[i-1]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k
 
# sol = Solution()

# nums = [0,0,1,1,1,2,2,3,3,4]
# k = sol.removeDuplicates(nums)
# print(k, nums[:k])  

# --------------------------------------------------------------------------  LeetCode Problem 58: Length of Last Word

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i = len(s) - 1
#         length = 0

#         while i >= 0 and s[i] == ' ':
#             i -= 1

#         while i >= 0 and s[i] != ' ':
#             length += 1
#             i -= 1

#         return length

# -------------------------------------------------------------------------- LeetCode Problem 125: Valid Palindrome

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1

#         while left < right:
        
#             while left < right and not s[left].isalnum():
#                 left += 1

#             while left < right and not s[right].isalnum():
#                 right -= 1

#             if s[left].lower() != s[right].lower():
#                 return False

#             left += 1
#             right -= 1

#         return True

# -------------------------------------------------------------------------- LeetCode Problem 136: Single Number

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = 0
#         for num in nums:
#             result ^= num
#         return result

# --------------------------------------------------------------------------