# import math

# def lcm(a, b):
#     return abs(a * b) // math.gcd(a, b)

# print(lcm(12, 15))

 
# import math

# print(math.lcm(12, 15))
# Xndir 1


# start = 1
# end = 100

# even_count = 0
# odd_count = 0

# for num in range(start, end + 1):
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers :", odd_count)
# Xndir 2



# n = 40
# a, b = 0, 1
# fib = []

# while a <= n:
#     fib.append(a)
#     a, b = b, a + b

# print("Fibonacci numbers from 0 to 40:", ", ".join(map(str, fib)))
# Xndir3


# s = input("Enter a string: ")

# digits = sum(ch.isdigit() for ch in s)
# letters = sum(ch.isalpha() for ch in s)

# print("Digits:", digits)
# print("Letters:", letters)
# Xndir4


# number = 73421
# digit_sum = sum(int(d) for d in str(number))
# print(digit_sum) 
# Xndir5



# n_input = input("Enter a non-negative integer: ")

# try:
#     n = int(n_input)
#     if n < 0:
#         print("Factorial is not defined for negative numbers.")
#     else:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         print(f"{n}! = {result}")
# except ValueError:
#     print("Invalid input. Please enter an integer.")
# Xndir6


# def check_conditions():
#     try:
#         age = int(input("Enter age: ").strip())
#     except ValueError:
#         print("Invalid age. Please enter a number.")
#         return

#     sex = input("Enter sex: ").strip().lower()

#     if 18 <= age <= 20 and sex in ('male', 'm', 'man'):
#         print("Condition met: age is between 18 and 20 and sex is male.")
#     else:
#         print("Condition not met.")

# if __name__ == '__main__':
#     check_conditions()
# Xndir7


# def tip_calculator():
#     try:
#         bill = float(input("Enter bill amount: "))
#         tip_pct = float(input("Enter tip percentage (e.g., 15 for 15%): "))

#         tip = bill * (tip_pct / 100.0)
#         total = bill + tip

#         print(f"Tip: ${tip:.2f}")
#         print(f"Total: ${total:.2f}")
#     except ValueError:
#         print("Please enter valid numbers for bill amount and tip percentage.")

# if __name__ == "__main__":
#     tip_calculator()

# ----------------------------------------------------------------------------------------------

# def is_palindrome(s: str) -> bool:
#     s = ''.join(ch.lower() for ch in s if ch.isalpha())
#     return s == s[::-1]

# def count_vowels(s: str) -> int:
#     vowels = set('aeiou')
#     return sum(1 for ch in s.lower() if ch in vowels)

# def main():
#     text = input("Enter a line of text: ")
#     normalized = ''.join(ch.lower() for ch in text if ch.isalpha())
#     palindrome = normalized == normalized[::-1]
#     print(f"Palindrome: {palindrome}")
#     print(f"Cleaned length: {len(normalized)}")
#     print(f"Vowels: {count_vowels(normalized)}")

# if __name__ == "__main__":
#     main()
# Xndir8 TEYAVCHARY TOKOSI BAJANOX HASHVICH, Toxy chishte e te sxal dzaynavornery ev qani taric e baxkacac teqsty.











