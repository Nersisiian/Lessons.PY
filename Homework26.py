# ---------------------------------------------- №1

# class Century:

#     def __init__(self, year):
#         self.year = year

#     def get_century(self):
#         return (self.year - 1) // 100 + 1

# c = Century(1900)
# print(c.get_century())   

# c = Century(1901)
# print(c.get_century())  

# c = Century(1)
# print(c.get_century()) 

# ---------------------------------------------- №2

# class Palindrome:
#     def __init__(self, inputString):
#         self.inputString = inputString.lower()

#     def is_palindrome(self):
#         return self.inputString == self.inputString[::-1]

# p1 = Palindrome("aabaa")
# print(p1.is_palindrome())  

# p2 = Palindrome("abac")
# print(p2.is_palindrome())  

# ---------------------------------------------- №3

# class Largest:
#     def __init__(self, inputList):
#         self.inputList = inputList

#     def max_adjacent_product(self):
#         max_product = float('-inf')

#         for i in range(len(self.inputList) - 1):
#             product = self.inputList[i] * self.inputList[i + 1]
#             if product > max_product:
#                 max_product = product

#         return max_product

# lst = Largest([3, 6, -2, -5, 7, 3])
# print(lst.max_adjacent_product())   


# ---------------------------------------------- №4

# class HighestWord:
#     def __init__(self, inputList):
#         self.inputList = inputList

#     def all_longest_strings(self):
#         max_len = max(len(word) for word in self.inputList)
#         return [word for word in self.inputList if len(word) == max_len]

# hw = HighestWord(["aba", "aa", "ad", "vcd", "aba"])
# print(hw.all_longest_strings())  


# ---------------------------------------------- №5

class Lucky:
    def __init__(self, n):
        self.n = str(n)  

    def is_lucky(self):
        s = self.n
        half = len(s) // 2

        left = sum(int(x) for x in s[:half])
        right = sum(int(x) for x in s[half:])

        return left == right

print(Lucky(1230).is_lucky())     
print(Lucky(239017).is_lucky())  

# ---------------------------------------------- №6

# def sortByHeight(a):
#     people = sorted([x for x in a if x != -1])
#     idx = 0
#     result = []

#     for x in a:
#         if x == -1:
#             result.append(-1)
#         else:
#             result.append(people[idx])
#             idx += 1
#     return result

# print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))

# ---------------------------------------------- №7

# def alternating_sums(a):
#     team1 = 0
#     team2 = 0
#     for i, weight in enumerate(a):
#         if i % 2 == 0:
#             team1 += weight  
#         else:
#             team2 += weight  
#     return [team1, team2]

# a = [50, 60, 60, 45, 70]
# print(alternating_sums(a))  


# ----------------------------------------------








