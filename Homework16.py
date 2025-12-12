# ----------------------------------------------------------------------------- No85

# def calculate_hypotenuse(a, b):

#     return (a**2 + b**2) ** 0.5

# def main():
#     a = float(input("Введите длину первого катета: "))
#     b = float(input("Введите длину второго катета: "))
#     hypotenuse = calculate_hypotenuse(a, b)
#     print(f"Длина гипотенузы: {hypotenuse:.2f}")

# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------- No88

# def find_median(a, b, c):

#     numbers = [a, b, c]
#     numbers.sort()
#     return numbers[1]

# def main():
#     try:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
#         num3 = float(input("Введите третье число: "))
#     except ValueError:
#         print("Пожалуйста, введите корректные числовые значения.")
#         return

#     median = find_median(num1, num2, num3)
#     print(f"Медиана введенных чисел: {median}")

# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------- No91-92

# def is_leap_year(year):

#     return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

# def ordinalDate(day, month, year):

#     month_days = [31, 28 + is_leap_year(year), 31, 30, 31, 30,
#                   31, 31, 30, 31, 30, 31]

#     if month < 1 or month > 12:
#         raise ValueError("Некорректный номер месяца")
#     if day < 1 or day > month_days[month - 1]:
#         raise ValueError("Некорректный номер дня")
#     total_days = sum(month_days[:month - 1]) + day
#     return total_days


# def dateFromOrdinal(ordinal_day, year):

#     leap = is_leap_year(year)
#     month_days = [31, 28 + leap, 31, 30, 31, 30,
#                   31, 31, 30, 31, 30, 31]
#     if ordinal_day < 1 or ordinal_day > (366 if leap else 365):
#         raise ValueError("Некорректный порядковый номер дня для данного года")
#     month = 1
#     while ordinal_day > month_days[month - 1]:
#         ordinal_day -= month_days[month - 1]
#         month += 1
#     day = ordinal_day
#     return day, month

# if __name__ == "__main__":
#     try:
#         day = int(input("Введите день: "))
#         month = int(input("Введите месяц: "))
#         year = int(input("Введите год: "))
#         ordinal = ordinalDate(day, month, year)
#         print(f"Порядковый номер даты: {ordinal}")
#         days_to_add = int(input("Введите количество дней для смещения: "))
#         new_ordinal = ordinal + days_to_add
#         max_days = 366 if is_leap_year(year) else 365
#         while new_ordinal > max_days:
#             new_ordinal -= max_days
#             year += 1
#             max_days = 366 if is_leap_year(year) else 365
#         new_day, new_month = dateFromOrdinal(new_ordinal, year)
#         print(f"Новая дата: {new_day}.{new_month}.{year}")

#     except ValueError as e:
#         print(f"Ошибка: {e}")

# ----------------------------------------------------------------------------- No94

# def can_form_triangle(a, b, c):

#     if a <= 0 or b <= 0 or c <= 0:
#         return False
   
#     if (a + b > c) and (a + c > b) and (b + c > a):
#         return True
#     else:
#         return False

# def main():
#     print("Введите длины сторон треугольника:")
#     try:
#         a = float(input("Длина стороны a: "))
#         b = float(input("Длина стороны b: "))
#         c = float(input("Длина стороны c: "))
#     except ValueError:
#         print("Ошибка ввода. Пожалуйста, вводите числовые значения.")
#         return

#     if can_form_triangle(a, b, c):
#         print("Да, из указанных сторон можно построить треугольник.")
#     else:
#         print("Нет, из указанных сторон построить треугольник невозможно.")

# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------- No101

# import random
# import string

# def generate_random_plate():
   
#     if random.choice([True, False]):
    
#         letters = ''.join(random.choices(string.ascii_uppercase, k=3))
#         digits = ''.join(random.choices(string.digits, k=3))
#         return f"{letters}{digits}"
#     else:
      
#         digits = ''.join(random.choices(string.digits, k=4))
#         letters = ''.join(random.choices(string.ascii_uppercase, k=3))
#         return f"{digits}{letters}"

# random_plate = generate_random_plate()
# print(random_plate)

# ----------------------------------------------------------------------------- No109

# def days_in_month(month, year):
    
#     if month < 1 or month > 12:
#         return "Некорректный номер месяца"
 
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         days[1] = 29  
    
#     return days[month - 1]

# month = int(input("Введите номер месяца (от 1 до 12): "))
# year = int(input("Введите год (например, 2023): "))
# result = days_in_month(month, year)
# print(f"Количество дней в месяце: {result}")

# def is_magic_date(day, month, year):
  
#     last_two_digits = year % 100
#     return (day * month) == last_two_digits

# magic_dates = []

# for year in range(1901, 2001):
#     for month in range(1, 13):
    
#         days_count = days_in_month(month, year)
#         for day in range(1, days_count + 1):
#             if is_magic_date(day, month, year):
#                 magic_dates.append((day, month, year))
# print("Магические даты в XX веке:")
# for date in magic_dates:
#     print(f"{date[0]:02d}.{date[1]:02d}.{date[2]}")

# ----------------------------------------------------------------------------- 

