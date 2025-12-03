# -----------------------------------------------------------------------------------------

# data = {
#     'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':4
# }

#  {
#      2:['a', 'b', 'c'], 3:['d', 'e'], 4:['f'] 
#  }

# -----------------------------------------------------------------------------------------

# data = {
#     'a': 2,
#     'b': 2,
#     'c': 2,
#     'd': 3,
#     'e': 3,
#     'f': 4
# }

# result = {}

# for key, value in data.items():

#     if value in result:
#         result[value].append(key)
#     else:
        
#         result[value] = [key]

# print(result)

# for value, keys in result.items():
#     print(f'{value}: {keys}')

# -----------------------------------------------------------------------------------------

# def is_prime(n):

#     if n <= 1:
#         return False  
#     if n <= 3:
#         return True  
#     if n % 2 == 0 or n % 3 == 0:
#         return False  

#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6  

#     return True

# number = int(input("Введите число: "))
# if is_prime(number):
#     print(f"{number} - Простое число")
# else:
#     print(f"{number} - Составное число")

# -----------------------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------------------





