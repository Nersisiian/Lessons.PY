# a = int(input("Enter first integer: "))
# b = int(input("Enter second integer: "))

# if a >= b:
#     print("Greatest:", a)
# else:
#     print("Greatest:", b)

 
# a = int(input("Enter first integer: "))
# b = int(input("Enter second integer: "))

# print("Greatest:", max(a, b))
# Xndir1


# ages = []

# for i in range(3):
#     while True:
#         try:
#             age = int(input(f"Enter age for person {i+1}: "))
#             if age < 0:
#                 print("Age cannot be negative. Please enter a valid age.")
#                 continue
#             ages.append(age)
#             break
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

# oldest = max(ages)
# youngest = min(ages)

# oldest_people = [i+1 for i, a in enumerate(ages) if a == oldest]
# youngest_people = [i+1 for i, a in enumerate(ages) if a == youngest]

# print(f"Oldest age: {oldest} (Person(s): {', '.join(map(str, oldest_people))})")
# print(f"Youngest age: {youngest} (Person(s): {', '.join(map(str, youngest_people))})")
# Xndir2


# def reverse_number(n: int) -> int:
#     sign = 1
#     if n < 0:
#         sign = -1
#         n = -n
#     rev = 0
#     while n > 0:
#         rev = rev * 10 + (n % 10)
#         n //= 10
#     return sign * rev


# x = int(input("Input: "))
# print("Output:", reverse_number(x))
# Xndir 3


# def main():
#     age_input = input("Enter age: ").strip()
#     sex = input("Enter sex (M/F): ").strip().upper()
#     marital = input("Enter marital status (Y/N): ").strip().upper()  


#     try:
#         age = int(age_input)
#     except ValueError:
#         print("ERROR")
#         return

#     if sex == 'F':
#         print("Urban areas")
#     elif sex == 'M':
#         if 20 <= age <= 40:
#             print("Anywhere")
#         elif 40 <= age <= 60:
#             print("Urban areas")
#         else:
#             print("ERROR")
#     else:
#         print("ERROR")

# if __name__ == "__main__":
#     main()
# Xndir4


# import random

# choices = ["камень", "ножницы", "бумага"]

# def determine_winner(user, comp):
#     if user == comp:
#         return "ничья"
#     if (user == "камень" and comp == "ножницы") or \
#        (user == "ножницы" and comp == "бумага") or \
#        (user == "бумага" and comp == "камень"):
#         return "победа"
#     return "поражение"

# def main():
#     print("Добро пожаловать в Камень-Ножницы-Бумага!")
#     print("Введите камень, ножницы или бумага. Введите 'выход' чтобы завершить.")

#     while True:
#         user_input = input("Ваш ход: ").strip().lower()
#         if user_input == "выход":
#             print("Спасибо за игру!")
#             break
#         if user_input not in choices:
#             print("Неправильный ввод. Попробуйте снова: камень, ножницы или бумага.")
#             continue

#         comp = random.choice(choices)
#         result = determine_winner(user_input, comp)

#         print(f"Компьютер: {comp}")
#         if result == "ничья":
#             print("Ничья!")
#         elif result == "победа":
#             print("Вы победили!")
#         else:
#             print("Вы проиграли!")

# if __name__ == "__main__":
#     main()
# Xndir 5


# import random

# def main():
#     try:
#         user_followers = int(input("Enter your follower count: "))
#     except ValueError:
#         print("Please enter a valid integer for followers.")
#         return

#     pc_followers = random.randint(0, 1000000)  # PC's random followers
#     print(f"PC followers: {pc_followers}")

#     if user_followers >= pc_followers * 1.20:
#         print("You are the blogger.")
#     else:
#         print("PC is the blogger.")

# if __name__ == "__main__":
#     main()
# Xndir 6


# distance_km = 12.0
# pc_time_min = 3.0

# pc_speed_km_per_min = distance_km / pc_time_min
# your_time_min = pc_time_min * 1.10
# your_speed_km_per_min = distance_km / your_time_min
# your_speed_km_per_hour = your_speed_km_per_min * 60

# print("PC speed (km/h):", pc_speed_km_per_min * 60)
# print("Your speed (km/h):", your_speed_km_per_hour)
# Xndir 7


