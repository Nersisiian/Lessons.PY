# x = int(input("x = "))
# for i in range(0,x+1):
#     for j in range(0,x*2+1):
#         if j <= i:
#             print(x - j + 1, end = "")
#         elif j >= 2 * x - i:
#             print(j - x + 1 , end="")  
#         else:
#             print(".",end="")
#     print()  
# ------------------------------------------
# n = int(input('Enter n: '))
# count = 0 
# for _ in range(n):
#     number = int(input('Enter number: '))
#     for i in range(2, number):
#         if number % i == 0:
#             break
#     else:
#         count += 1
# print(count)
# ------------------------------------------
# n = int(input('Enter n: ')) 
# summ = 0
# for i in range(1, n + 1):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     summ += factorial
# print(summ)
# ------------------------------------------
# n = int(input('Enter n: '))
# max_sum = 0
# for i in range(n):
#     number = int(input('Enter number: '))
#     summ = 0
#     for j in str(number):
#         summ += int(j)
#     if summ > max_sum:
#         max_sum = summ
# print(max_sum)
# ------------------------------------------
# n = int(input('Enter number: '))
# for i in range(1, n + 1):
#     k = 0
#     for j in range(1, n + 1):
#         if j <= i:
#             print(n - k, end='')
#             k += 1
#         else:
#             print('.', end='')
#     k -= 1
#     for j in range(n, 0, -1):
#         if j <= i:
#             print(n - k, end='')
#             k -= 1
#         else:
#             print('.', end='')
#     print()
# ------------------------------------------


import msvcrt
import random
import os

a = int(input("enter a: "))
b = int(input("enter b: "))
monkeyI = random.randint(1, a - 2)
monkeyJ = random.randint(1, b - 2)
bananaI = random.randint(1, a - 2)
bananaJ = random.randint(1, b - 2)

while True:
    x = msvcrt.getwche().lower()
    if x == "a":
        monkeyJ -= 1
    elif x == "d":
        monkeyJ += 1
    elif x == "w":
        monkeyI -= 1
    elif x == "s":
        monkeyI += 1
    else:
        break
    os.system('cls')
    for i in range(0, a):
        for j in range(0, b):
            if j == 0 or j == b - 1:
                print("|", end=" ")
            elif i == 0 or i == a - 1:
                print("-", end=" ")
            elif i == monkeyI and j == monkeyJ:
                print("🐒", end="")
            elif i == bananaI and j == bananaJ and bananaI != monkeyI:
                print("🍌", end="")
            else:
                print(".", end=" ")
        print()