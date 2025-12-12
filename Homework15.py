# ----------------------------------------------------------------------------- No1

# year = 1900
# century = (year + 99) // 100
# print(century)

# ----------------------------------------------------------------------------- No2

# inputString = input()
# inputString = inputString.lower()
# is_palindrome = inputString == inputString[::-1]
# print(is_palindrome) 

# ----------------------------------------------------------------------------- No3

# inputList = [3, 6, -2, -5, 7, 3]
# max_product = inputList[0] * inputList[1]

# for i in range(1, len(inputList)):
#     current_product = inputList[i - 1] * inputList[i]
#     if current_product > max_product:
#         max_product = current_product

# print(max_product)

# ----------------------------------------------------------------------------- No4

# inputList = ["aba", "aa", "ad", "vcd", "aba"]
# max_length = max(len(s) for s in inputList)
# allLongestStrings = [s for s in inputList if len(s) == max_length]

# print(allLongestStrings)

# ----------------------------------------------------------------------------- No5

# n = input("Enter the ticket number: ")

# if len(n) % 2 != 0:
#     print("Ticket number should have an even number of digits.")
# else:
#     half_length = len(n) // 2
#     first_half = n[:half_length]
#     second_half = n[half_length:]
#     sum_first = 0
#     for digit in first_half:
#         sum_first += int(digit)
#     sum_second = 0
#     for digit in second_half:
#         sum_second += int(digit)

#     if sum_first == sum_second:
#         print("Lucky(n) = true")
#     else:
#         print("Lucky(n) = false")

# ----------------------------------------------------------------------------- No6

# a = [-1, 150, 190, 170, -1, -1, 160, 180]
# people = [height for height in a if height != -1]
# people.sort()
# index = 0
# for i in range(len(a)):
#     if a[i] != -1:
#         a[i] = people[index]
#         index += 1
# print(a)

# ----------------------------------------------------------------------------- No7

# a = [50, 60, 60, 45, 70]
# team1_sum = 0
# team2_sum = 0

# for i in range(len(a)):
#     if i % 2 == 0:
#         team1_sum += a[i]
#     else:
#         team2_sum += a[i]
# result = [team1_sum, team2_sum]
# print(result)

# ----------------------------------------------------------------------------- HappyNumber

# n = 19
# seen_numbers = set()
# current_number = n

# while True:

#     sum_of_squares = 0
#     temp = current_number
#     while temp > 0:
#         digit = temp % 10
#         sum_of_squares += digit * digit
#         temp //= 10

#     if sum_of_squares == 1:
#         print(True)
#         break

#     if sum_of_squares in seen_numbers:
#         print(False)
#         break

#     seen_numbers.add(sum_of_squares)
#     current_number = sum_of_squares

# -----------------------------------------------------------------------------





