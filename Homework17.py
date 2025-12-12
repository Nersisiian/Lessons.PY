# ---------------------------------------------------------No1

# import time
# import os

# def run_lengths(seq):
    
#     if not seq:
#         return []
#     res = []
#     i = 0
#     n = len(seq)
#     while i < n:
#         j = i + 1
#         while j < n and seq[j] == seq[i]:
#             j += 1
#         res.append(j - i)
#         i = j
#     return res

# def clear_console():
   
#     os.system('cls' if os.name == 'nt' else 'clear')

# def print_steps_and_final(seq):
   
#     nxt = run_lengths(seq)
#     print(nxt)
#     time.sleep(0.7)  
#     clear_console()  
#     if nxt:
#         if len(nxt) > 1:
#             print_steps_and_final(nxt)  
#         else:
#             print("Финальный ответ:", nxt)

# if __name__ == "__main__":
#     x = [2, 2, 2, 3, 1, 4, 4, 5, 7, 1, 2, 2, 2, 3, 3]
#     print_steps_and_final(x)

# ----------------------------------------------------------No1 2Tarberak

# def run_lengths(seq):
    
#     if not seq:
#         return []
#     res = []
#     i = 0
#     n = len(seq)
#     while i < n:
#         j = i + 1
#         while j < n and seq[j] == seq[i]:
#             j += 1
#         res.append(j - i)
#         i = j
#     return res

# def print_steps_and_final(seq):
    
#     nxt = run_lengths(seq)
#     print(nxt)
    
#     if len(nxt) > 1:
#         print_steps_and_final(nxt)

# if __name__ == "__main__":
#     x = [2, 2, 2, 3, 1, 4, 4, 5, 7, 1, 2, 2, 2, 3, 3]
#     print_steps_and_final(x)

#     # Финальный вывод
#     final_result = run_lengths(x)
#     while len(final_result) > 1:
#         final_result = run_lengths(final_result)

#     print("Финальный ответ:", final_result)

# ---------------------------------------------------------- No2

# def count_consecutive(lst, index=0, count=1, result=None):
#     if result is None:
#         result = []

#     if index == len(lst) - 1:
#         result.append(lst[index])
#         result.append(count)
#         return result

#     if lst[index] == lst[index + 1]:
#         count += 1
#     else:
#         result.append(lst[index])
#         result.append(count)
#         count = 1  

#     return count_consecutive(lst, index + 1, count, result)

# x = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
# result = count_consecutive(x)
# print(result)

# ----------------------------------------------------------No3

# def longest_common_prefix(strs):
#     if not strs:
#         return ""
    
#     def recursive_lcp(s1, s2, index):
#         if index >= len(s1) or index >= len(s2) or s1[index] != s2[index]:
#             return s1[:index]
#         return recursive_lcp(s1, s2, index + 1)

#     prefix = strs[0]
#     for i in range(1, len(strs)):
#         prefix = recursive_lcp(prefix, strs[i], 0)
#         if prefix == "":
#             break
    
#     return prefix

# mylist = ['flower', 'flow', 'flight']
# result = longest_common_prefix(mylist)
# print(result)  

# ----------------------------------------------------------