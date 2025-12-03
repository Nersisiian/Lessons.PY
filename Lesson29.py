# -------------------------------------------------------------------

# class VowelPrinter:
#     def __init__(self, text, vowels):
#         self.text = text

#         self.vowel_map = {}
#         i = 0
#         while i < len(vowels):
#             self.vowel_map[vowels[i]] = True
#             i += 1

#     def print_vowels(self):
#         i = 0
#         while i < len(self.text):     
#             ch = self.text[i]
#             is_vowel = self.vowel_map.get(ch)  
#             print(ch, bool(is_vowel))
#             i += 1


# text = 'barikplekoabzippjokllau'
# x = 'aeiou'

# vp = VowelPrinter(text, x)
# vp.print_vowels()

# ------------------------------------------------------------------- Leetcode 88 Merge Sorted Array

# from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
#         i = m - 1
#         j = n - 1
#         k = m + n - 1

#         while j >= 0:
#             if i >= 0 and nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1

# sol = Solution()

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# sol.merge(nums1, m, nums2, n)
# print(nums1)  

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# sol.merge(nums1, m, nums2, n)
# print(nums1)  

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# sol.merge(nums1, m, nums2, n)
# print(nums1)

# ------------------------------------------------------------------- Leetcode 27 Remove Element

# from typing import List

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0  
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]  
#                 k += 1
#         return k

# sol = Solution()

# nums = [3,2,2,3]
# val = 3
# k = sol.removeElement(nums, val)
# print(k, nums[:k])  

# nums = [0,1,2,2,3,0,4,2]
# val = 2
# k = sol.removeElement(nums, val)
# print(k, nums[:k])  

# ------------------------------------------------------------------- Leetcode 26 Remove Duplicates from Sorted Array

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

# --------------------------------------------------- Leetcode 80 Remove Duplicates from Sorted Array II

# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 2:
#             return n
        
#         k = 2  
#         for i in range(2, n):
            
#             if nums[i] != nums[k - 2]:
#                 nums[k] = nums[i]
#                 k += 1
#         return k

# --------------------------------------------------- Leetcode 169 Majority Element

# from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += 1 if num == candidate else -1
#         return candidate

# sol = Solution()

# nums = [3,2,3]
# print(sol.majorityElement(nums)) 

# nums = [2,2,1,1,1,2,2]
# print(sol.majorityElement(nums))  

# ---------------------------------------------------      




