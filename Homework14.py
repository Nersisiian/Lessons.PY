# -------------------------------------------------------------------------------

# def is_balanced(text):
    
#     opening = '([{'
#     closing = ')]}'
#     stack = []
 
#     for char in text:
#         if char in opening:  
#             stack.append(char)  
#         elif char in closing:  
#             if not stack: 
#                 return False
#             top = stack.pop() 
            
#             if (top == '(' and char != ')') or \
#                (top == '[' and char != ']') or \
#                (top == '{' and char != '}'):
#                 return False

#     return len(stack) == 0

# print(is_balanced('(){}[]'))  
# print(is_balanced('(())[{[]}]'))  
# print(is_balanced('({[)]}'))  
# print(is_balanced('((()))'))  
# print(is_balanced('(()'))  

# -------------------------------------------------------------------------------

# def check_list(mylist):
#     index = 0
#     length = len(mylist)

#     while True:
       
#         if index < 0 or index >= length:
#             return False
        
#         if index == length // 2:
#             return True
        
#         next_index = mylist[index]
#         index = next_index
# mylist = [3, 2, 0, 1, 2]
# result = check_list(mylist)
# print(result)

# -------------------------------------------------------------------------------

# x = [
#     [1, 2, 3],
#     [6, 5, 4],
#     [7, 8, 9]
# ]

# result = []
# if not x:
#     print(result)
# top, bottom, left, right = 0, len(x) - 1, 0, len(x[0]) - 1

# while top <= bottom and left <= right:

#     for i in range(left, right + 1):
#         result.append(x[top][i])
#     top += 1

#     for i in range(top, bottom + 1):
#         result.append(x[i][right])
#     right -= 1

#     if top <= bottom:
#         for i in range(right, left - 1, -1):
#             result.append(x[bottom][i])
#         bottom -= 1

#     if left <= right:
#         for i in range(bottom, top - 1, -1):
#             result.append(x[i][left])
#         left += 1
# print(result)

# -------------------------------------------------------------------------------

# list1 = [7, 4, 1, 2, 3, 6, 5]
# list2 = [2, 3, 6]
# len1 = 0
# len2 = 0

# def calculate_length(lst):
#     count = 0
#     for _ in lst:
#         count += 1
#     return count

# len1 = calculate_length(list1)
# len2 = calculate_length(list2)
# is_sublist = False

# for i in range(len1 - len2 + 1):  
#     match = True
#     for j in range(len2):  
#         if list1[i + j] != list2[j]:
#             match = False
#             break
#     if match:
#         is_sublist = True
#         break

# if is_sublist:
#     print("list2 является подсписком list1.")
# else:
#     print("list2 не является подсписком list1.")

# -------------------------------------------------------------------------------






